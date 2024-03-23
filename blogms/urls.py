
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('admin/', admin.site.urls),
     path('base/', views.BASE, name='base'),
     path('', views.INDEX, name='home'),
     path('Blog/', views.BLOG, name='blog'),
     path('SingleBlog/<str:id>', views.SINGLE_BLOG, name='single_blog'),
     
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
