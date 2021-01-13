from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from listing.models import Listing

User = get_user_model()


class BidOnListing(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bidder")
    amount = models.FloatField(default=0.0)

    listing = models.ForeignKey("listing.Listing", on_delete=models.PROTECT, related_name="bids_on_listing")

    # Timestamp
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.bidder

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Bid on auction'
        verbose_name_plural = 'Bid on auctions'


class Auction(models.Model):
    FAILED = 0
    SUCCESS = 1
    AUCTION_STATUS = (
        (FAILED, 'Failed'),
        (SUCCESS, 'Success')
    )
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name="auction_seller")
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="auction_buyer")

    # It will change to listing model as a foreign key and also for bid.
    listing = models.ForeignKey("listing.Listing", on_delete=models.PROTECT)
    bid = models.ForeignKey(BidOnListing, on_delete=models.PROTECT)

    buyer_amount_percentage = models.FloatField(default=0.0)
    seller_amount_percentage = models.FloatField(default=0.0)

    status = models.PositiveIntegerField(choices=AUCTION_STATUS, default=SUCCESS)

    # Timestamp
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.seller

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Auction Detail'
        verbose_name_plural = 'Auction Details'


@receiver(post_save, sender=BidOnListing)
def perform_celery_task_on_bid(sender, instance, created, **kwargs):
    if created:
        listing = Listing.objects.get(pk=instance.listing.pk)
        expires = listing.expires_on
        now = timezone.now()
        if now < expires:
            updated_expires_on = now + timezone.timedelta(hours=1)
            listing.expires_on = updated_expires_on
            listing.save()
