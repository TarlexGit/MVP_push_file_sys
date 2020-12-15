from django.shortcuts import render
from rest_framework.views import APIView
from account.models import UserVerificationToken
from rest_framework import status
from rest_framework.response import Response
from .serializers import CheckToken
# class ChekUserTokenFromClient

class ChekUserTokenFromClient(APIView):
    def get(self, request, format=None): 
        token = request.query_params['token']
        # allqueryset = UserVerificationToken.objects.all 
        queryset = UserVerificationToken.objects.filter(token=token).exists()
        if queryset: 
            print(queryset)
            return Response(status.HTTP_200_OK)
        else:
            print('ex')
            return Response(status=status.HTTP_404_NOT_FOUND) 
        # if queryset:
        # return Response(status=status.HTTP_200_OK)
        # else:
        
        # return Response(status=status.HTTP_404_NOT_FOUND)  
