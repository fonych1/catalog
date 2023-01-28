from django.contrib import admin
from django.urls import path, include

import notifications.urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('', include('catalog.urls', namespace='catalog')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('openapi/', get_schema_view(
        title="Catalog API",
        description="API description"
    ), name='openapi-schema'),
]

