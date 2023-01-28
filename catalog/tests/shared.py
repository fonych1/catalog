from typing import Any

from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

from catalog.views import ProductView


class AnyValue:
    def __eq__(self, other):
        return True


any_value = AnyValue()


def create_product(client: APIRequestFactory, user: User, new_product: dict[str, Any]) -> str:
    view = ProductView.as_view({'post': 'create'})

    request = client.post('/catalog/', data=new_product)
    force_authenticate(request, user=user)
    response = view(request)

    return response.data['id']


def get_product(client: APIRequestFactory, user: User, product_id: str) -> list:
    view = ProductView.as_view({'get': 'retrieve'})

    request = client.get('/catalog/')
    force_authenticate(request, user=user)
    response = view(request, pk=product_id)

    return response.data if response.status_code == 200 else None
