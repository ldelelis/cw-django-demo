from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from apps import handlers
from apps.models import App
from apps.serializers import AppSerializer, DomainRecordInputSerializer


class AppViewset(viewsets.ModelViewSet):
    queryset = App.objects.all()

    def get_serializer_class(self):
        if self.action == "update_domain_record":
            return DomainRecordInputSerializer
        return AppSerializer

    def perform_update(self, serializer):
        print("i create a deployment on k8s, trust me")
        return super().perform_update(serializer)

    @action(detail=True, methods=['PATCH'])
    def update_domain_record(self, request, pk=None):
        handler = handlers.AppHandler()
        handler.update_domain_record(request.data.get('new_record'))
        return Response({}, 204)
