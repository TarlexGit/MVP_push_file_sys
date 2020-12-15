from django.db import models
from django.contrib.auth.models import User
from django.contrib.messages.storage import default_storage

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename> 
    return 'UFiles/user_{0}/{1}'.format(instance.client_id.id, filename)


class UpFiles(models.Model):
    client_id = models.ForeignKey(User, verbose_name="Аккаунт", 
        on_delete=models.CASCADE,
        null=True,
        default=None)
    request_data = models.FileField(upload_to=user_directory_path)  
    content = models.TextField(null = True, blank = True)

