from django.urls import path
from .views import CategoryListCreate, CategoryDetail, PostListCreate, PostDetail, TagListCreate, TagDetail,  AboutListCreate, AboutDetail,  YoutubeListCreate, YoutubeDetail

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('tags/', TagListCreate.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
   
    path('about/', AboutListCreate.as_view(), name='about-list-create'),
    path('about/<int:pk>/', AboutDetail.as_view(), name='about-detail'),

    path('youtube/', YoutubeListCreate.as_view(), name='youtube-list-create'),
    path('youtube/<int:pk>/', YoutubeDetail.as_view(), name='youtube-detail'),
]
