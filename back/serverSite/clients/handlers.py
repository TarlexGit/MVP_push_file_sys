from clients.services import FileService
from protos import client_pb2_grpc
 
def grpc_handlers(server):
    client_pb2_grpc.add_UpFilesControllerServicer_to_server(FileService.as_servicer(), server) 