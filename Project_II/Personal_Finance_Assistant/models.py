from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Info(models.Model):
    user_id = models.CharField(max_length=10,default=0)
    user_name = models.CharField(max_length=50,default=0)
    password = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.user_id
    


class IncomeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    finance= models.CharField(max_length=20,default='income')

    def __str__(self):
        return f"{self.title} - {self.amount}"
