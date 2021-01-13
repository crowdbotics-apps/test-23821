import os

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import AutoSlugField

# Create your models here.
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField


def list_category_image_path(instance, filename):
    return os.path.join(
        'listing_categories/category_%s' % instance.id, filename
    )


class ListingCategory(models.Model):
    title = models.CharField(_('Title'), max_length=120, default=None, null=False, blank=False)
    slug = AutoSlugField(_('Slug'), populate_from='title', unique=True, null=False, default=None, blank=False)
    image = models.ImageField(_('Image'), upload_to=list_category_image_path, default=None, null=True, blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})

    description = RichTextUploadingField(_('Description'),
                                         config_name='listing_categories',
                                         null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Listing Category'
        verbose_name_plural = 'Listing Categories'
