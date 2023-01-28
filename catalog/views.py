from rest_framework import authentication, viewsets

from .permissions import CatalogPermission
from catalog.models import Product
from catalog.serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    permission_classes = (CatalogPermission,)
    authentication_classes = (authentication.BasicAuthentication,)
    serializer_class = ProductSerializer
    model = Product
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
