from django.contrib import admin
from auction.models import Auction, BidOnListing


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['seller', 'buyer', 'listing', 'bid', 'status', 'created', 'updated']


@admin.register(BidOnListing)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['bidder', 'amount', 'listing', 'created', 'updated']
