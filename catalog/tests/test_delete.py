import pytest
from typing import Any

from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

from .shared import create_product, get_product
from catalog.views import ProductView


@pytest.mark.django_db
def test_delete_product(drf_client: APIRequestFactory, drf_superuser: User, new_product: dict[str, Any]):
    product_id = create_product(drf_client, drf_superuser, new_product)

    view = ProductView.as_view({'delete': 'destroy'})

    request = drf_client.delete('/catalog/')

    # 401 if no user
    response = view(request, pk=product_id)
    assert response.status_code == 401

    # success with superuser
    force_authenticate(request, user=drf_superuser)
    response = view(request, pk=product_id)

    assert response.status_code == 204

    product = get_product(drf_client, drf_superuser, product_id)

    assert product is None
