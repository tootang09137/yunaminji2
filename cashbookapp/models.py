from email.policy import default
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Cashbook(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank =True, default='')
    likes = models.PositiveIntegerField(default=0, verbose_name='추천수')
    clicks = models.PositiveIntegerField(default=0, verbose_name='조회수') 

    def __str__(self):
        return self.title