from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=200, default='')
    zip_code = models.IntegerField(default=0)
    country = models.CharField(max_length=100, default='')
    card_holder = models.CharField(max_length=100, default='')
    card_number = models.IntegerField(default=1234123412341234)
    cvc = models.IntegerField(default=123)
    expiration_month = models.CharField(max_length=100, default='DECEMBER')
    expiration_year = models.IntegerField(default=2021)
    picture = models.ImageField(upload_to='profile', null=True)
    password_key = models.CharField(max_length=50, default='')

    def __str__(self):
        return ('Profile belonging to {}'.format(self.user))


class Payment_keys(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    payment_method_key = models.CharField(max_length=150, default='')
    customer_Id = models.CharField(max_length=150, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.user.username
