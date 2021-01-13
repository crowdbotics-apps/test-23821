from django.urls import path
from . import views as newsletterview

urlpatterns = [
    path('newsletter-signup',newsletterview.newsletter_signup,name='news-signup'),
    path('newsletter-signup-complete',newsletterview.signup_complete,name='signup-comp'),
]