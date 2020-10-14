from django.db import models
from  api import generate
from django.conf import settings

# Create your models here.


class Cisco(models.Model):
    sap_id = models.CharField(max_length=32, unique=True)
    hostname = models.CharField(max_length=100,null=True,blank=True,unique=True)
    loopback = models.CharField(max_length=100,null=True,blank=True,unique=True)
    mac_address = models.CharField(max_length=100,null=True,blank=True,unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified = models.DateTimeField(auto_now=True,null=True, blank=True)
 
    def __str__(self):
        return self.user.username
    
    def check_unique(self, sap_id):
        return not Cisco.objects.filter(sap_id=sap_id).exists()

    def save(self, *args, **kwargs):
        if not self.sap_id:
            self.sap_id = generate.generate_unique_sapid(self, 10)
        super(Cisco, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
    