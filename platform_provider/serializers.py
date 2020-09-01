from rest_framework import serializers

from platform_provider.models import PlatformProvider


class PlatformProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformProvider
        fields = '__all__'


class BulkUpdateSerializer(serializers.ListSerializer):
    def update(self, instances, validated_data):
        id_hash_mapping = {index: instance for index, instance in enumerate(instances)}

        result = [
            self.child.update(id_hash_mapping[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]

        return result


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformProvider
        fields = '__all__'
        list_serializer_class = BulkUpdateSerializer

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
