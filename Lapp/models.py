from Library.settings import MEDIA_ROOT
from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Book(models.Model):
    ISBN=models.IntegerField()
    Title=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Edition=models.CharField(max_length=20)
    Publication=models.CharField(max_length=100)
    ImageBook=models.ImageField(upload_to='photos')    
    Borrowing_period=models.IntegerField()  
    Status=BooleanField(default=True,null=True,blank=True)
   
    def __str__(self):
        return   self.Title
  