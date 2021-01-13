from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from auction.forms import BidOnListingForm
from auction.models import BidOnListing, Auction


class AuctionFormView(ListView):
    model = Auction


class BidOnListingView(ListView):
    model = BidOnListing
    template_name = 'auction/bid_on_listing_list.html'


class BidOnListingCreateView(CreateView):
    model = BidOnListing
    form_class = BidOnListingForm
    template_name = 'auction/bid_on_listing_create.html'
    success_url = reverse_lazy('auction_bid_create')


class BidOnListingDetailView(DetailView):
    model = BidOnListing

