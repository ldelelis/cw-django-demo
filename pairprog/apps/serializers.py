from rest_framework import serializers

from apps.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"


class DomainRecordInputSerializer(serializers.Serializer):
    new_record = serializers.CharField(max_length=250)
