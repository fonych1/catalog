import pytest
from typing import Any

from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User

from .shared import create_product
from catalog.views import ProductView


@pytest.mark.django_db
def test_get_products(drf_client: APIRequestFactory, drf_superuser: User, new_product: dict[str, Any]):
    product_id = create_product(drf_client, drf_superuser, new_product)

    view = ProductView.as_view({'get': 'list'})

    request = drf_client.get('/catalog/')
    response = view(request)

    assert response.status_code == 200
    assert response.data == [
        {
            "id": product_id,
            "sku": "test_sku",
            "name": "test_name",
            "price": "100.00",
            "brand": "test_brand"
        }
    ]
