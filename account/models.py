from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    image_file = models.FileField(upload_to='documents/user_img/', blank=True, null=True)
    name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length=150)
    
    def __str__(self):
        return (f"{self.username}")
    
    
class Account(models.Model):
    account_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=16)
    money = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    
    def __str__(self):
        return (f"владец:{self.account_owner}, название счета: {self.account_name}")
