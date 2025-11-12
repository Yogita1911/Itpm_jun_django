from django.db import models

# Create your models here.
class Python_Jun(models.Model):
    Name = models.TextField(max_length=50)
    Address =models.TextField(max_length=50)
    Email = models.EmailField(unique=True)
    Marks = models.IntegerField()
    Subject = models.TextField(max_length=50)
    Fees = models.DecimalField(max_digits=10,decimal_places=2,default=10000.0)
    Role_Number = models.AutoField(primary_key=True)

    

    
