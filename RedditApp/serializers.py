from .models import *
from rest_framework import serializers


class SubblueitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subblueit
        fields = ('name', 'followers', 'id')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('sub', 'title', 'pub_date', 'karma', 'text', 'author', 'id')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'text', 'pub_date', 'karma', 'author', 'id')

class UserSerializer(serializers.ModelSerializer):
    # subs = serializers.PrimaryKeyRelatedField(many=True, queryset=Subblueit.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username')
