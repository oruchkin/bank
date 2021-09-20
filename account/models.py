from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    image_file = models.FileField(upload_to='documents/user_img/', blank=True, null=True)
    name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length=150)
    
    
