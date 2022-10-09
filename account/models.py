from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=10)
    age = models.IntegerField(null= True, blank= True)
    address = models.CharField(max_length=50, null= True, blank= True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    def __str__(self):
        return self.username