import datetime
from email.policy import default
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Cashbook(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    detail = models.TextField()
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now, editable=False)
    image = models.ImageField(upload_to = 'images/', blank =True, default='')
    likes = models.PositiveIntegerField(default=0, verbose_name='추천수')
    clicks = models.PositiveIntegerField(default=0, verbose_name='조회수') 

    def __str__(self):
        return self.title

    def clean(self):
        title = self.title
        if title == "":
            raise ValidationError("글을 작성해주세요")
        return super(Cashbook,self).clean()

    def clean_content(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.content
        else:
            return self.cleaned_data['content']