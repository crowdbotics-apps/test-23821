"""proud_forest_23287 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("home.urls")),
    path("", include("listing.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("accounts/", include("users.auth_urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("chat/", include("chat.urls")),
    path("chat_user_profile/", include("chat_user_profile.urls")),
    path('',include('auction_app.urls')),
    path('',include('notification_app.urls')),
    path('',include('newsletter_app.urls')),
    path("payments/", include("payments.urls", namespace="payments")),
    path("auction/", include("auction.urls")),
    path("api/v1/", include([
        path("rest-auth/", include("rest_auth.urls")),
        # Override email confirm to use allauth's HTML view instead of rest_auth's API view
        path("rest-auth/registration/account-confirm-email/<str:key>/", confirm_email),
        path("rest-auth/registration/", include("rest_auth.registration.urls")),
        path("", include("home.api.v1.urls")),
        path("chat/", include("chat.api.v1.urls")),
        path("", include("chat_user_profile.api.v1.urls")),
        path("users/", include("users.api.v1.urls")),
        path("categories/", include("categories.api.v1.urls")),
    ]))
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



admin.site.site_header = "Proud Forest"
admin.site.site_title = "Proud Forest Admin Portal"
admin.site.index_title = "Proud Forest Admin"

# swagger
api_info = openapi.Info(
    title="Proud Forest API",
    default_version="v1",
    description="API documentation for Proud Forest App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
