from django.shortcuts import get_object_or_404
from .models import Product


class ProductViewTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        if (
                request.method == 'GET'
                and request.path.startswith('/catalog/')
                and request.path != '/catalog/'
                and request.user.is_anonymous
        ):
            product_id = request.path.split('/')[-2]
            product = get_object_or_404(Product, id=product_id)
            product.requested += 1
            product.save()

        return response
