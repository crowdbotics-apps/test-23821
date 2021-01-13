from rest_framework import serializers
from categories.models import *


class ListingCategoriesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(source='image_thumbnail', read_only=True)

    class Meta:
        model = ListingCategory
        fields = '__all__'
