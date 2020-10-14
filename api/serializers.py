from rest_framework import serializers
from .models import Cisco


class CiscoSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Cisco
        fields = ('sap_id','hostname','loopback','mac_address')
