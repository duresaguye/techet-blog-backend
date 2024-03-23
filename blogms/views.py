from django.shortcuts import render,redirect,HttpResponse
from authentication.models import Post


def BASE(request):
    return render(request,'main/base.html')

def INDEX(request):

   latest_post =Post.objects.order_by('-id')[0:12]
   
   
   context = {
        
        'latest_post':latest_post,
        
        
    }
       
   return render(request,'main/index.html',context)

def BLOG(request):
   popular_post =Post.objects.order_by('-id')[0:40]
   editorpick_post =Post.objects.filter(section='Editor_Pick').order_by('-id')[0:9]
   recent_post =Post.objects.filter(section='Recent').order_by('-id')[0:9]
   trending_post =Post.objects.filter(section='Trending').order_by('-id')[0:9]
   inspirational_post =Post.objects.filter(section='Inspiration').order_by('-id')[0:9]
   latest_post =Post.objects.filter(section='Latest Posts').order_by('-id')[0:9]
   main_post =Post.objects.filter(main_post = True)[0:40]
   
   context = {
        'popular_post':popular_post,
        'editorpick_post':editorpick_post,
        'recent_post':recent_post,
        'trending_post':trending_post,
        'inspirational_post':inspirational_post,
        'latest_post':latest_post,
        'main_post':main_post,
        
    }
    
   return render(request,'main/blog.html',context)






def SINGLE_BLOG(request,id):
    post = Post.objects.filter(id=id)
    
    context = {
         'post':post,
    }

    return render(request,'main/single_blog.html',context)