from django.urls import path
from . import views as auctionview

urlpatterns = [
    path('my-auctions',auctionview.auctions,name='auctions'),
]