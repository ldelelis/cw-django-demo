from buckets.serializers import BucketInputSerializer
from rest_framework import viewsets

from buckets.models import Bucket


class BucketViewset(viewsets.ModelViewSet):
    queryset = Bucket.objects.all()
    serializer_class = BucketInputSerializer
