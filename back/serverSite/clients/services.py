from .models import UpFiles   
from django_grpc_framework.services import Service    
from protos import client_pb2_grpc, client_pb2
from django.contrib.auth.models import User  
from .serializers import UpFilesProtoSerializer
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from settings.settings import BASE_DIR
import io, os
from account.models import UserVerificationToken
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from posixpath import isfile
   
# a8715eae41f2a4bf342874bb07cf7d74982c40a1
class FileService(Service):    
    def Create(self, request_iterator, context): 
        SERVER_ID = 1
        metadata = dict(context.invocation_metadata()) 

        print("BidirectionalStreamingMethod called by client...")  
        for first_request in request_iterator:
            client = first_request.client_token
            user = UserVerificationToken.objects.get(token=client).user

            name_file = first_request.file_name.split('/')[-1] # split for filename from path
            path_to_file = 'UFiles/user_{0}/{1}'.format(user, name_file) 
            
            try:
                UpFiles.objects.get(request_data=path_to_file)
                return
            except: 
                # pass
                buf = io.StringIO()   

                for request in request_iterator:   
                    buf.write(request.request_data.rstrip().decode()) 
                yield client_pb2.Response( 
                    response_data=("Server: upload file done = {}".format(first_request.file_name))) 
                cc = ContentFile(buf.getvalue()) 
                
                default_storage.save(path_to_file, cc) 
                path = default_storage.save(path_to_file, cc) 
                
                new_f = default_storage.open(path) 
                
                file_content = buf.getvalue()
                UpFiles.objects.create(client_id=user,request_data=path_to_file, content=file_content)  
                buf.close()
                default_storage.delete(path) 
        print("------- BidirectionalStreamingMethod stop -------")  
 
        