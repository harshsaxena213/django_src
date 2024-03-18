from django.db import models

class vege_data(models.Model):
    name=models.CharField(max_length=15)
    desc=models.TextField()
    pic=models.ImageField()
    
    def  __str__(self):
        return self.name

    