import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,HttpResponse
from authentication.models import Youtube
from authentication.models import Question  
from authentication.models import Post


def BASE(request):
    return render(request,'main/base.html')

def INDEX(request):
    latest_post = Post.objects.order_by('id')  # Order by a timestamp field
    
    context = {
        'latest_post': latest_post,
    }
    
    return render(request, 'main/index.html', context)


def BLOG(request):
    popular_post = Post.objects.order_by('id')
    editorpick_post = Post.objects.filter(section='Editor_Pick').order_by('id')
    recent_post = Post.objects.filter(section='Recent').order_by('id')
    trending_post = Post.objects.filter(section='Trending').order_by('id')
    inspirational_post = Post.objects.filter(section='Inspiration').order_by('id')
    latest_post = Post.objects.filter(section='Latest Posts').order_by('id')
    main_post = Post.objects.filter(main_post=True)
    
    context = {
        'popular_post': popular_post,
        'editorpick_post': editorpick_post,
        'recent_post': recent_post,
        'trending_post': trending_post,
        'inspirational_post': inspirational_post,
        'latest_post': latest_post,
        'main_post': main_post,
    }
    
    return render(request, 'main/blog.html', context)







def SINGLE_BLOG(request,id):
    post = Post.objects.filter(id=id)
    
    context = {
         'post':post,
    }

    return render(request,'main/single_blog.html',context)
def podcast(request):
    videos = Youtube.objects.order_by('-id').all()  # Order videos by the id field in descending order
    return render(request, 'main/podcast.html', {'videos': videos})



@csrf_exempt
def quize(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        question_id = data.get('questionId')
        answer = data.get('answer')

        # Process the answer (e.g., check correctness, store in database, etc.)
        # For demonstration purposes, simply returning a JSON response
        response_data = {'success': True, 'message': 'Answer submitted successfully'}
        return JsonResponse(response_data)
    else:
        # Fetch questions from the database for rendering the quiz page
        questions = Question.objects.all()
        context = {'questions': questions}
        return render(request, 'main/Quize.html', context)

  
   

def services(request):

    return render(request, 'main/Services.html')

def about(request):
    return render(request, 'main/About.html')


