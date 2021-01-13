from django.urls import path, re_path
from . import views as loginview
from allauth.account import views as allauth_account_views

urlpatterns = [
    path('', loginview.home, name='home'),
    path('signup/', loginview.signup, name='signup'),
    path('login/', loginview.login, name='login'),
    path('logout/', loginview.logout, name='logout'),
    path('reset-password/', loginview.reset_password_first, name='reset1'),
    path('new-password/<str:key>', loginview.reset_password_second, name='reset2'),
    path("confirm-email/", allauth_account_views.email_verification_sent,
         name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", allauth_account_views.confirm_email,
            name="account_confirm_email"),

    # password reset
    path("password/reset/", allauth_account_views.password_reset,
         name="account_reset_password"),
    path("password/reset/done/", allauth_account_views.password_reset_done,
         name="account_reset_password_done"),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            allauth_account_views.password_reset_from_key,
            name="account_reset_password_from_key"),
    path("password/reset/key/done/", allauth_account_views.password_reset_from_key_done,
         name="account_reset_password_from_key_done"),
    path('profile/', loginview.profile_page, name='profile'),
    path('save-profile/', loginview.save_profile, name='save-profile'),

]
