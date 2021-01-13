from django.db import models
from categories.models import ListingCategory

# Create your models here.
from users.models import User

PACKAGES = [
    {
        0: {'seller_price': 85, 'buyer_percentage': 4.5, "min": 150, "max": 4500},
        1: {'seller_price': 45, 'buyer_percentage': 4.5, "min": 150, "max": 4500},
        2: {'seller_price': 45, 'buyer_percentage': 4.5, "min": 150, "max": 4500},
        3: {'seller_price': 125, 'buyer_percentage': 4.5, "min": 150, "max": 4500},
    }
]
REGULAR = 0
NO_RESERVE = 1
RETURNING = 2
ROYALTY = 3
LISTING_TYPE = (
    (REGULAR, 'Regular'),
    (NO_RESERVE, 'No Reserve'),
    (RETURNING, 'Returning'),
    (ROYALTY, 'Royalty'),
)
TYPE_CHOICES = (
    ('S', 'Select'),
    ('I', 'Input'),
    ('T', 'Textarea'),
    ('C', 'Checkbox'),
)
STEP_CHOICE = (
    ('N', 'None'),
    ('M', 'Make'),
    ('B', 'Basic'),
    ('D', 'Detail'),
)

MAKE_CHOICE = (
    (1, 'Volve'),
    (2, 'BMW'),
)

MODEL_CHOICE = (
    (1, 'CS6'),
    (2, 'CS7'),
    (3, 'CS8'),
    (4, 'CS9'),
)


class ListingPlan(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    seller_price = models.FloatField(null=True, blank=True)
    buyer_percentage = models.FloatField(null=True, blank=True)
    min = models.FloatField(null=True, blank=True)
    max = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    listing_type = models.PositiveIntegerField(choices=LISTING_TYPE, default=REGULAR)

    def __str__(self):
        return self.name


class Listing(models.Model):
    category = models.ForeignKey(ListingCategory, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    image = models.ImageField(upload_to='media/listing_images')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    manufacture_year = models.CharField(max_length=10, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    make = models.PositiveIntegerField(choices=MAKE_CHOICE, blank=True, null=True)
    model = models.PositiveIntegerField(choices=MODEL_CHOICE, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    expires_on = models.DateTimeField(null=True, blank=True, )
    is_expired = models.BooleanField(default=False, blank=True, null=True)
    plan = models.ForeignKey(ListingPlan, on_delete=models.CASCADE, null=True)
    is_approved = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name


class OptionList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ListingFaq(models.Model):
    question = models.CharField(max_length=500, help_text="Question that display in the form")

    input_type = models.CharField(max_length=1, default=TYPE_CHOICES[1], choices=TYPE_CHOICES,
                                  help_text="Select type of Questions")
    sort_order = models.PositiveSmallIntegerField(help_text="Question are display on the base of Sort order Number")
    category = models.ForeignKey(ListingCategory, on_delete=models.CASCADE,
                                 help_text="Select category where this Questions display")
    option = models.ManyToManyField(OptionList, blank=True,
                                    help_text="This option used when your input type select , radio or checkbox")
    step_choice = models.CharField(max_length=1, default=STEP_CHOICE[0], choices=STEP_CHOICE,
                                   help_text="Add step if you want to display Question in specific step")
    required = models.BooleanField(default=False,
                                   help_text="Checked if this Questions required")

    def __str__(self):
        return self.question


class ListingFaqAttached(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, )
    listing_faq = models.ForeignKey(ListingFaq, on_delete=models.CASCADE, )
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.answer


class ListingImages(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media/listing_images')

    def __str__(self):
        return self.listing.name
