from rest_framework import status
from rest_framework.reverse import reverse
import json
import pytest

# Create your tests here.
from platform_provider.models import PlatformProvider

TEST_SIZE = 10000


@pytest.fixture
def platforms():
    platforms = []
    for i in range(TEST_SIZE):
        platforms.append(PlatformProvider.objects.create(
            name=f'name_{i}',
            country=f'country_{i}',
            kind=f'kind_{i}')
        )

    return platforms


@pytest.mark.django_db
def test_list_serializer(client, platforms):
    test_url = reverse(
        "bulk-update",
    )
    data = [{
        'name': f'{x.name} - {x.id}',
        'country': f'Country - {x.id + 1}',
        'id': x.id,
    } for x in platforms]

    response = client.put(
        test_url,
        data=json.dumps(data),
        content_type='application/json',
    )

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == TEST_SIZE
