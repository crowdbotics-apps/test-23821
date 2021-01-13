from django.urls import path, include
from .views import *

app_name = "payments"
urlpatterns = [
    path('stripe/', include("djstripe.urls", namespace="djstripe")),
    path('add-payment-method/', UserSavePaymentMethod.as_view()),
]
