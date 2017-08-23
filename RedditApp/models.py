from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Use makemigrations and migrate to edit the models and databases for this dir
class Subblueit(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    followers = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    sub = models.ForeignKey(Subblueit, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(timezone.now())
    karma = models.IntegerField(default=0)
    text = models.CharField(max_length=400, blank=True)
    user = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.title

    def was_posted_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    karma = models.IntegerField(default=0)
    user = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
