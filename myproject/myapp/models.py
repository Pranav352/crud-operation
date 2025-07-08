from django.db import models

# Create your models here.



class Employee(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    email=models.EmailField(unique=True,blank=True,null=True)
    address=models.TextField()
    phone=models.IntegerField()

    def __str__(self):
        return self.name