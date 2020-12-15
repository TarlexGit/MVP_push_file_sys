from django.db import models
from django.contrib.auth.models import User
import os, binascii
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver

def generate_key():
    length = 20
    while True: 
        new_key = binascii.hexlify(os.urandom(length)).decode() 
        if UserVerificationToken.objects.filter(token=new_key).count()==0:
            break
    return new_key

# Create your models here.
class UserVerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=20, unique=True)

@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        UserVerificationToken.objects.create(user = instance, token=generate_key())