from django.contrib import admin
from listing.models import Listing, ListingFaq, OptionList, ListingFaqAttached, ListingPlan,ListingImages


# Register your models here.


class ListingFaqAdmin(admin.ModelAdmin):
    list_filter = ('input_type',)
    list_display = ('question', 'input_type', 'category', 'required')


class ListingFaqAttachedAdmin(admin.ModelAdmin):
    list_display = ('listing_faq', 'answer')


class ListingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Listing)
admin.site.register(ListingFaq, ListingFaqAdmin)
admin.site.register(OptionList)
admin.site.register(ListingPlan, ListingPlanAdmin)
admin.site.register(ListingFaqAttached, ListingFaqAttachedAdmin)
admin.site.register(ListingImages)
