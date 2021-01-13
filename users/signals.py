from django.db.models.signals import pre_save, post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import User


@receiver(post_save, sender=User)
def create_stripe_customer(sender, created, instance, **kwargs):
    print(instance)
