from django.shortcuts import render
from .models import Cisco
from rest_framework import viewsets
from .serializers import CiscoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
# Create your views here.
class CiscoViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()
    queryset = Cisco.objects.all()
    serializer_class = CiscoSerializer

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cannot create the view like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cannot update the view like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CiscoSerializer(instance)
        return Response(serializer.data)


    