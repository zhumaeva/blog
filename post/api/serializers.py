from rest_framework import serializers
from post.models import Tag, Category, Post


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'slug',)


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug',)


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
