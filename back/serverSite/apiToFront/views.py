from django.shortcuts import render 
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UpFilesSerializer,TokenSerializer
from clients.models import UpFiles
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from account.models import UserVerificationToken

class UserFilesViewSet(viewsets.ViewSet): 
    permission_classes = (IsAuthenticated, )
    def list(self, request):
        queryset = UpFiles.objects.filter(client_id=request.user)
        serializer = UpFilesSerializer(queryset, many=True)
        return Response(serializer.data)
 
class GetUserToken(APIView):
    def get(self, request, format=None):
        queryset = UserVerificationToken.objects.filter(user=request.user)
        serializer = TokenSerializer(queryset, many=True)
        return Response(serializer.data)
