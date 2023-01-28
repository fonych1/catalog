import pytest

from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User


@pytest.fixture
def drf_superuser() -> User:
    user = User.objects.create_superuser(username='superuser')
    return user


@pytest.fixture
def drf_client() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture
def new_product():
    return {
        "sku": "test_sku",
        "name": "test_name",
        "price": 100,
        "brand": "test_brand"
    }
