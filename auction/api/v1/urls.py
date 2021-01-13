from django.urls import path, include
from rest_framework.routers import DefaultRouter


# from auction.api.v1.viewsets import (
# )

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
]
