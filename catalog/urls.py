from django.urls import path, include

from rest_framework.routers import DefaultRouter

from catalog.views import ProductView

app_name = "catalog"

router = DefaultRouter()

router.register('catalog', ProductView, basename='catalog view')

urlpatterns = [
    path(r'', include(router.urls)),
]
