from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Use makemigrations and migrate to edit the models and databases for this dir
class Subblueit(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    followers = models.IntegerField(default=0)
    # creator = models.ForeignKey('auth.User', related_name='subs', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    sub = models.ForeignKey(Subblueit, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(timezone.now())
    karma = models.IntegerField(default=0)
    text = models.CharField(max_length=400, blank=True)
    # urlfield for links?
    author = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    karma = models.IntegerField(default=0)
    author = models.ForeignKey('auth.User', null=True)
    # parent = models.ForeignKey('self', null=True, related_name='replies')
    def __str__(self):
        return self.text

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    subs = models.ManyToManyField(Subblueit)
