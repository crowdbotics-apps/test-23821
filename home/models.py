from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class PageFAQ(models.Model):
    title = models.CharField(_('Title'), max_length=500, default=None, null=False, )
    description = RichTextUploadingField(_('Description'),
                                         config_name='listing_categories',
                                         null=True, blank=True)
    is_published = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
