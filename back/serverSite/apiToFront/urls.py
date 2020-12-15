from django.urls import include, path 
from clients.handlers import grpc_handlers as client_grpc_handlers 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserFilesViewSet,GetUserToken


# api/users/ ->
urlpatterns = [ 
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/files/',UserFilesViewSet.as_view({'get': 'list'})),
    path('user/token/', GetUserToken.as_view()),
]