from django.db import models
class Books(models.Model):

     bookname=models.CharField(max_length=15)
     author=models.CharField(max_length=20)
     category=models.CharField(max_length=15)
     price=models.IntegerField(max_length=15)
     photo=models.ImageField(upload_to='Books/',null=True,blank=True)    

     def __str__(self):
          return self.name
     

# Create your models here.
