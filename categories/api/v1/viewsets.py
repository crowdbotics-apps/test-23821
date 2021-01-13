from rest_framework import viewsets
from .serializers import *


class ListingCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ListingCategoriesSerializer
    queryset = ListingCategory.objects.all().order_by('title')
