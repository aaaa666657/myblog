from django.db import models
from django.utils import timezone

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

class Activity(models.Model):
    name = models.CharField(max_length=255,verbose_name='活動名稱')
    date = models.DateTimeFiel(verbose_name='活動時間')
    place = models.CharField(max_length=255,verbose_name='活動地點')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
