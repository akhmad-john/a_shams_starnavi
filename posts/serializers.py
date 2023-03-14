from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_by', 'likes')


class LikeSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ('post_id', 'user_id')
        
        
class LikeByDaySerializer(serializers.ModelSerializer):
    day = serializers.DateField()
    likes = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ('day', 'likes')
