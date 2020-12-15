from django.contrib import admin
from django.urls import include, path 
from clients.handlers import grpc_handlers as client_grpc_handlers
from . import settings 
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apiToFront.urls')), 
    path('api/clients/', include('clients.urls')), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
def grpc_handlers(server):
    client_grpc_handlers(server)
 
 