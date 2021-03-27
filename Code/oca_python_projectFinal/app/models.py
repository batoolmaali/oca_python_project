from django.db import models  

#for auth
from django.contrib.auth.models import User

class Product(models.Model):  
    # eid = models.CharField(max_length=20)  
    name = models.CharField(max_length=100)  
    des = models.CharField(max_length=255)  
    typeskin = models.CharField(max_length=255)  
    time = models.CharField(max_length=100)  
    image = models.FileField()
    class Meta:  
        db_table = "product"  

#for auth
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)

