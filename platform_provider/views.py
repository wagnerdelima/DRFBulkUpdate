from rest_framework import generics, permissions
from rest_framework.response import Response

from platform_provider.models import PlatformProvider
from platform_provider.serializers import PlatformProviderSerializer, PlatformSerializer


class ListPlatformProviders(generics.ListAPIView):
    serializer_class = PlatformProviderSerializer

    def get_queryset(self):
        return PlatformProvider.objects.all()


class BulkUpdateView(generics.UpdateAPIView):
    permission_classes = (
        permissions.AllowAny,
    )
    queryset = PlatformProvider.objects.all()
    lookup_field = 'id'
    serializer_class = PlatformSerializer

    def get_queryset(self, ids=None):
        return PlatformProvider.objects.filter(id__in=ids)

    def update(self, request, *args, **kwargs):
        ids = [int(platform['id']) for platform in request.data]
        instances = self.get_queryset(ids=ids)
        serializer = self.get_serializer(
            instances, data=request.data, partial=True, many=True
        )
        print(f'>>> {serializer.is_valid()}')
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data)
