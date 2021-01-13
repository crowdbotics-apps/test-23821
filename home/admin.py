from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(PageFAQ)
class PageFAQAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'created', 'updated']
    list_editable = ['is_published']
    readonly_fields = ['created', 'updated']
