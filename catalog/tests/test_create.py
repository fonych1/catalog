import pytest
from typing import Any

from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

from .shared import any_value
from catalog.views import ProductView


@pytest.mark.django_db
def test_create_product(drf_client: APIRequestFactory, drf_superuser: User, new_product: dict[str, Any]):
    view = ProductView.as_view({'post': 'create'})

    request = drf_client.post('/catalog/', data=new_product)

    # 401 if no user
    response = view(request)
    assert response.status_code == 401

    # success with superuser
    force_authenticate(request, user=drf_superuser)
    response = view(request)

    assert response.status_code == 201
    assert response.data == {
        "id": any_value,
        "sku": "test_sku",
        "name": "test_name",
        "price": "100.00",
        "brand": "test_brand"
    }
