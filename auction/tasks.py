from celery import shared_task
from django.utils import timezone

from auction.models import Auction, BidOnListing
from django.core.mail import send_mail
from proud_forest_23287.celery import app
from listing.models import PACKAGES, Listing


@app.task
def send_email_on_auction():
    now = timezone.now()
    all_listing = Listing.objects.filter(is_expired=False)
    for listing in all_listing:
        expires_on = listing.expires_on
        reserve = PACKAGES[0][listing.listing_type]
        winner_bid = BidOnListing.objects.filter(listing=listing).order_by('-created').first()
        if now > expires_on:
            print(f"expiring the list {listing.name}")
            buyer_percentage = reserve.get("buyer_percentage")
            buyer_min = reserve.get("min")  # Min limit to get from buyer as per list type selected
            buyer_max = reserve.get("max")  # Max limit to get from buyer as per list type selected
            bidder_percentage_amount = winner_bid.amount * 0.05  # Buyer percentage amount to deduct

            # Apply limits for amount to deduct from buyer
            amount_to_deduct_from_buyer = bidder_percentage_amount
            if bidder_percentage_amount < buyer_min:
                amount_to_deduct_from_buyer = buyer_min
            elif bidder_percentage_amount > buyer_max:
                amount_to_deduct_from_buyer = buyer_max

            # Amount that is to be deduct from seller
            seller_amount_deduct = reserve.get("seller_price")

            if winner_bid.amount > reserve.get("seller_price"):
                auction = Auction.objects.create(
                    seller=winner_bid.listing.user,
                    buyer=winner_bid.bidder,
                    listing=winner_bid.listing,
                    bid=winner_bid,
                    status=1,
                    buyer_amount_percentage=amount_to_deduct_from_buyer,
                    seller_amount_percentage=seller_amount_deduct
                )
            else:
                auction = Auction.objects.create(
                    seller=winner_bid.listing.user,
                    buyer=winner_bid.bidder,
                    listing=winner_bid.listing,
                    bid=winner_bid,
                    status=0,
                    buyer_amount_percentage=amount_to_deduct_from_buyer,
                    seller_amount_percentage=seller_amount_deduct
                )
            listing.is_expired = True
            listing.save()


# @shared_task
# def send_email_on_auction(bid):
#     try:
#         bid_on_listing = BidOnListing.objects.get(pk=bid)
#         list_type = bid_on_listing.listing.listing_type
#         reserve = PACKAGES[0][list_type]
#         if bid_on_listing.amount > reserve.get("seller_price"):
#             auction = Auction.objects.create(
#                 seller=bid_on_listing.listing.user,
#                 buyer=bid_on_listing.bidder,
#                 listing=bid_on_listing.listing,
#                 bid=bid,
#                 status=1
#             )
#         else:
#             auction = Auction.objects.create(
#                 seller=bid_on_listing.listing.user,
#                 buyer=bid_on_listing.bidder,
#                 listing=bid_on_listing.listing,
#                 bid=bid,
#                 status=0
#             )
#             # send email to buyer for wining the bid along with seller details
#             send_mail('AUCTION', f'You have successfully won the auction. \n'
#                                  f' This is seller details:\n Email: {auction.seller.email}\n'
#                                  f'Contact No: {bid_on_listing.listing.phone_number}',
#                       'sender@example.com', [auction.buyer.email])
#
#             # send email to seller for some action on listing along with buyer details
#             send_mail('AUCTION',
#                       f'You have successfully won the auction. \n'
#                       f' This is buyer details:\n Email: {auction.buyer.email}\n'
#                       f'Contact No: {bid_on_listing.listing.phone_number}',
#                       'sender@example.com',
#                       [auction.seller.email])
#
#     except BidOnListing.DoesNotExist():
#         pass
