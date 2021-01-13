from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import *

router = DefaultRouter()
router.register('listing-categories', ListingCategoryViewSet, basename='listing-categories')

urlpatterns = [
    path('', include(router.urls)),
]
