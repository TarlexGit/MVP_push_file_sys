import grpc
from proto import client_pb2, client_pb2_grpc
from pathlib import Path, PurePath 
import sys
import os, io
import hashlib 
 

CHUNK_SIZE = 1024
CLIENT_ID =2
class FileClient:
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.stub = client_pb2_grpc.UpFilesControllerStub(channel)

    def upload(self,in_file_name, client):   
        print(
            "--------------Call BidirectionalStreamingMethod Begin---------------")  
 
        # create a generator
        def request_messages():  
            yield client_pb2.Request( 
                client_token=client,
                file_name=in_file_name)
            
            with open(in_file_name, 'rb+') as f:  
                while True: 
                    piece = f.read(1024)
                    if len(piece) == 0:
                        break 
                    yield client_pb2.Request(
                        client_token=client,
                        file_name=in_file_name,
                        request_data=piece)   
        
        response_iterator = self.stub.Create(request_messages())
        for response in response_iterator:
            print("1 recv from server, message=%s" %
                (response.response_data))
        
        print("--------------Call BidirectionalStreamingMethod Over---------------")
  
  
 