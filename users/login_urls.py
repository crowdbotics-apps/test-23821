from django.urls import path
from . import views as loginview

urlpatterns = [
    path('',loginview.home,name='home'),
    path('signup',loginview.signup,name='signup'),
    path('signin',loginview.login,name='login'),
    path('signout',loginview.logout,name='logout'),
    path('reset-password',loginview.reset_password_first,name='reset1'),
    path('new-password/<str:key>',loginview.reset_password_second,name='reset2'),
    path('profile',loginview.profile_page,name='profile'),
    path('save-profile',loginview.save_profile,name='save-profile'),
]