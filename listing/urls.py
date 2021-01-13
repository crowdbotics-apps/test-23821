from django.urls import path

from listing.views import AddListing, SelectPlan

urlpatterns = [
    path("<str:plan>/add-listing", AddListing.as_view(), name="add_listing"),
    path("select-plan", SelectPlan.as_view(), name="select_plan"),
]
