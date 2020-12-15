from django.urls import include, path 
from clients.handlers import grpc_handlers as client_grpc_handlers 

from .views import ChekUserTokenFromClient


urlpatterns = [  
    path('client/token/', ChekUserTokenFromClient.as_view()),
]