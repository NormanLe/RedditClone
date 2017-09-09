from .models import *
from rest_framework import serializers


class SubblueitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subblueit
        fields = ('name', 'followers', 'id')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('sub', 'title', 'pub_date', 'karma', 'text', 'author', 'id')
        view_name='RedditApp:post-detail',

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'text', 'pub_date', 'karma', 'author', 'id')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # subs = serializers.PrimaryKeyRelatedField(many=True, queryset=Subblueit.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username')
