from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from .models import *


# Register your models here.
class ListingCategoryForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ListingCategory
        fields = '__all__'


@admin.register(ListingCategory)
class ListingCategory(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated']
    form = ListingCategoryForm
