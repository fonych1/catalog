import pytest
from typing import Any

from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

from .shared import create_product, get_product
from catalog.views import ProductView


@pytest.mark.django_db
def test_update_product(drf_client: APIRequestFactory, drf_superuser: User, new_product: dict[str, Any]):
    product_id = create_product(drf_client, drf_superuser, new_product)

    view = ProductView.as_view({'put': 'update'})

    request = drf_client.put(f'/catalog/{product_id}/', data={
        "id": "1",
        "sku": "new_sku",
        "name": "new_name",
        "price": 120,
        "brand": "new_brand"
    })

    # 401 if no user
    response = view(request, pk=product_id)
    assert response.status_code == 401

    # success with superuser
    force_authenticate(request, user=drf_superuser)
    response = view(request, pk=product_id)
    assert response.status_code == 200

    expected_response = {
        "id": product_id,
        "sku": "new_sku",
        "name": "new_name",
        "price": "120.00",
        "brand": "new_brand"
    }

    assert response.data == expected_response

    product = get_product(drf_client, drf_superuser, product_id)

    assert product == expected_response
