from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from auction.models import BidOnListing, Auction


class BidOnListingForm(forms.ModelForm):
    class Meta:
        model = BidOnListing
        fields = ['bidder', 'amount', 'listing']

    def clean(self):
        cleaned_data = super(BidOnListingForm, self).clean()
        amount = cleaned_data.get('amount')
        listing = cleaned_data.get('listing')
        previous_bid = BidOnListing.objects.filter(listing=listing).order_by('-created').first()
        now = timezone.now()
        expires = listing.expires_on
        if now < expires and listing.is_expired is False:
            updated_expires_on = now + timezone.timedelta(hours=1)
            listing.expires_on = updated_expires_on
            listing.save()
            with_hold_amount = (amount * 0.05)
            if with_hold_amount < 250:
                raise ValidationError({"amount": f"5% of your bid must be greater then $250"})
            if with_hold_amount > 5000:
                with_hold_amount = 5000
            print(f"Amount to hold from account on bid: ${with_hold_amount}")
        else:
            raise ValidationError({"amount": "Listing expired."})
        if previous_bid:
            if amount <= previous_bid.amount:
                raise ValidationError({"amount": "Bid amount is less than previous bid."})
            if previous_bid.amount >= 1000:
                if amount - previous_bid.amount < 250:
                    raise ValidationError({"amount": "Your bid amount difference from previous bid is less than $250."})
        return cleaned_data


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['seller', 'buyer', 'listing', 'bid', 'status']
