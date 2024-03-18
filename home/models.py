from django.db import models

class studnets(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField(null=True)
    image=models.ImageField()
    email=models.EmailField()
    
    
class products(models.Model):
    price=models.IntegerField()
    name=models.TextField


    
    
    