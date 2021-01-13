from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from categories.models import ListingCategory
from listing.forms import ListingForm
from listing.models import ListingFaq, ListingFaqAttached, ListingImages

IMAGESERROR = {'required': 'This field is required', 'length': 'Max 5 images are allowed',
               'type': 'Invalid image type'}
from listing.models import ListingFaq, ListingFaqAttached, ListingPlan


class SelectPlan(generic.View):

    @staticmethod
    def get(request, *args, **kwargs):
        plans = ListingPlan.objects.all()
        return render(request, 'listing/selectPlan.html', {'plans': plans})

    @staticmethod
    def post(request, *args, **kwargs):
        data = request.POST
        if data['plan']:
            if ListingPlan.objects.filter(slug=data['plan']).first():
                return redirect(reverse('add_listing', kwargs={'plan': data['plan']}))

        plans = ListingPlan.objects.all()
        return render(request, 'listing/selectPlan.html', {'error': 'Please select plan', 'plans':plans})


class AddListing(generic.View):
    faq_id = {}
    faq_object = {}
    form = {}

    def get(self, request, *args, **kwargs):
        listing_plan = kwargs['plan']
        plan = ListingPlan.objects.filter(slug=listing_plan).first()
        if plan is None:
            return redirect(reverse('select_plan', kwargs={}))
        categories = ListingCategory.objects.all()
        for category in categories:
            self.update_faq_id(category)
            self.update_faq_object(category, basic_form=ListingForm)

        data = {'form': self.form, 'activeForm': '#cars', 'plan': plan}
        return render(request, 'listing/addListing.html', data)

    @staticmethod
    def get_option(i):
        option = []
        if i.option.all():
            option = [item.name for item in i.option.all()]
        return option

    def post(self, request, *args, **kwargs):
        image_error = []
        data = request.POST
        listing_form = ListingForm(request.POST, request.FILES)
        category = ListingCategory.objects.get(id=int(data['category_id']))
        plan = ListingPlan.objects.get(id=int(data['plan']))
        self.update_faq_id(category)
        faqs = ListingFaq.objects.filter(category=category)
        faq_is_valid = True
        for item in faqs:
            if item.required and self.get_answer(data=data, element=str(item.id)) == '':
                faq_is_valid = False
        image_is_valid = True
        images = request.FILES.getlist('image')
        no_of_images = 5

        if not images:
            image_error.append(IMAGESERROR['required'])
            image_is_valid = False

        if len(images) > no_of_images:
            image_error.append(IMAGESERROR['length'])
            image_is_valid = False

        for file in images:
            if 'image/' not in file.content_type:
                image_error.append(IMAGESERROR['type'])
                image_is_valid = False

        if listing_form.is_valid() and faq_is_valid and image_is_valid:
            listing = listing_form.save(commit=False)
            listing.user = request.user
            listing.category = category
            listing.plan = plan
            listing.save()
            images_objs = [ListingImages(image=e, listing=listing) for e in images]
            objs = [
                ListingFaqAttached(
                    listing_id=listing.id,
                    listing_faq_id=e,
                    answer=self.get_answer(data, str(e)),
                )
                for e in self.faq_id[category.slug]
            ]
            ListingImages.objects.bulk_create(images_objs)
            ListingFaqAttached.objects.bulk_create(objs)
        else:
            self.update_faq_object(category, data=data, basic_form=listing_form, error=True)
            data = {'form': self.form, 'activeForm': '#'+category.slug, 'plan': plan, 'error': image_error}

            return render(request, 'listing/addListing.html', data)

        self.update_faq_object(category, data=None, basic_form=ListingForm)
        data = {'form': self.form, 'activeForm': '#' + category.slug, 'plan': plan, 'success': True}

        return render(request, 'listing/addListing.html', data)

    @staticmethod
    def get_answer(data, element):
        value = ''
        if data:
            try:
                value = data[element]
            except:
                pass
        return value

    def update_faq_id(self, category):
        category_faq = ListingFaq.objects.filter(category=category)
        self.faq_id[category.slug] = []
        for i in category_faq:
            self.faq_id[category.slug].append(i.id)

    def update_faq_object(self, category, data=None, basic_form=None, error=False):
        category_object = ListingFaq.objects.filter(category=category)
        self.faq_object[category.slug] = []
        for i in category_object:
            value = self.get_answer(data=data, element=str(i.id))
            self.faq_object[category.slug].append({
                'type': i.input_type,
                'question': i.question,
                'option': self.get_option(i),
                'value': value,
                'id': i.id,
                'order': i.sort_order,
                'required': i.required,
                'error': i.required and error and value == "",
                'step': i.step_choice,
            })
        self.form[category.slug] = {
            'faq': self.faq_object[category.slug],
            'basic': basic_form,
            'category_id': category.id
        }
        self.form[category.slug]['faq'] = sorted(self.form[category.slug]['faq'], key=lambda i: i['order'])
