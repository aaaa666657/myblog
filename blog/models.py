from django.db import models
from django.utils import timezone

import uuid
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Tag(models.Model):
    contact = models.ForeignKey(Post,on_delete=models.CASCADE)
    name    = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Category(models.Model):
   name = models.CharField(max_length=255,verbose_name='活動名稱')
   users = models.ManyToManyField(User,verbose_name='使用者名單')
   created = models.DateTimeField(auto_now_add=True, editable=False)
   last_updated = models.DateTimeField(auto_now=True, editable=False)
   token = models.UUIDField(db_index=True, default=uuid.uuid4)

class Teacher(models.Model):
    name = models.CharField(max_length=255,verbose_name='老師名稱')

class ClassTable(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    weekday = models.IntegerField()
    period  = models.IntegerField()
    name    = models.CharField(max_length=255)

#    def __str__(self):
#        return self.name

