from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Group, Post, Comment, Follow, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        read_only=False,
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(queryset=Follow.objects.all(),
                                              fields=('user', 'following'))]
    
    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError('You cant follow yourself')
        return data
