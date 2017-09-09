from django import forms
from django.forms import ModelForm
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['pub_date', 'karma', 'author']

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=200, help_text='Required. Please enter a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

class CommentForm(ModelForm):
    comment = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Comment
        exclude = ['post', 'pub_date', 'karma', 'author', 'text',]
