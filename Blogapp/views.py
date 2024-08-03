from rest_framework import generics
from .models import Category, Post, Tag,  About,  Youtube
from Blogapp.serializers import CategorySerializer, PostSerializer, TagSerializer,  AboutSerializer,  YoutubeSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



class AboutListCreate(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer



class YoutubeListCreate(generics.ListCreateAPIView):
    queryset = Youtube.objects.all()
    serializer_class = YoutubeSerializer

class YoutubeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Youtube.objects.all()
    serializer_class = YoutubeSerializer
