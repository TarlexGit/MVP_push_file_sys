from clients.models import UpFiles 
from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import UserVerificationToken


class UpFilesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UpFiles
        fields = ('request_data', 'content',)


class TokenSerializer(serializers.ModelSerializer):
     class Meta:
         model = UserVerificationToken
         fields = ('token',)