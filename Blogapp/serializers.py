from rest_framework import serializers
from .models import Category, Post, Tag,  About,  Youtube

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'



class YoutubeSerializer(serializers.ModelSerializer):
    embed_url = serializers.SerializerMethodField()

    class Meta:
        model = Youtube
        fields = ['id', 'slug', 'status', 'is_recent', 'embed_url']

    def get_embed_url(self, obj):
        return obj.get_embed_url() 
