

from buckets.models import Bucket
from rest_framework import serializers


class BucketInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = "__all__"


class BucketOutputSerializer(serializers.ModelSerializer):
    ...



# class BucketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bucket
#         # fields = "__all__"
#         fields = [
#
#         ]
