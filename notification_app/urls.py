from django.urls import path
from . import views as notificationview

urlpatterns = [
    path('notifications',notificationview.notification_page,name='notifications'),
    path('preference-submit',notificationview.preference_submit,name='pref-submit'),
]