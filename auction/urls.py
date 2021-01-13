from django.urls import path

from auction.views import BidOnListingView, BidOnListingCreateView, BidOnListingDetailView, AuctionFormView

urlpatterns = [
    # Auction
    path("auction-list/", AuctionFormView.as_view(), name="auction_list"),

    # Bidding
    path("bid-list/", BidOnListingView.as_view(), name="auction_bid_list"),
    path("bid-create/", BidOnListingCreateView.as_view(), name="auction_bid_create"),
    path("bid-detail/<int:pk>/", BidOnListingDetailView.as_view(), name="auction_bid_detail"),
]
