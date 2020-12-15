from django_grpc_framework import proto_serializers
from clients.models import UpFiles
from protos import client_pb2 
from google.protobuf.json_format import MessageToDict, ParseDict
# from django_grpc.serializers import serialize_model
from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import UserVerificationToken

class UpFilesProtoSerializer(serializers.Serializer): 
    def message_to_data(self, message): 
        return MessageToDict(
            message, including_default_value_fields=True,
            preserving_proto_field_name=True
        )

    def data_to_message(self, data): 
        return ParseDict(
            data, self.Meta.proto_class(),
            ignore_unknown_fields=True
        )
  
      
    client_id = serializers.IntegerField()
    request_data = serializers.FileField()
    def create(self, **validated_data):
        return UpFiles.objects.create(**validated_data)
    class Meta:
        model = UpFiles
        # proto_class = client_pb2.Request
        fields = "__all__"


class CheckToken(serializers.Serializer):
    token = serializers.CharField(max_length=20)
    class Meta:
        model = UserVerificationToken
        # proto_class = client_pb2.Request
        fields = ('token',)