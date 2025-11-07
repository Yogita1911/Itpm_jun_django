from django.db import models

# Create your models here.
class Python_Jun(models.Model):
    Name = models.TextField(max_length=100)
    Address =models.TextField(max_length=200)
    Email = models.EmailField(unique=True)
    Marks = models.IntegerField()
    Subject = models.TextField(max_length=100)
    Role_Number = models.AutoField(primary_key=True)

    

    
