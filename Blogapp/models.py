from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Published'),
    )
    SECTION = (
        ('Programming', 'Programming'),
        ('Networking', 'Networking'),
        ('Trending', 'Trending'),
        ('Inspiration', 'Inspiration'),
        ('Latest Posts', 'Latest Posts'),
    )

    featured_image = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = RichTextField()
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    status = models.CharField(choices=STATUS, max_length=100)
    section = models.CharField(choices=SECTION, max_length=100)
    main_post = models.BooleanField(default=False)
    video_link = models.URLField(blank=True, null=True)  # Add this field for video links

    def __str__(self):
        return self.title

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver, Post)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Youtube(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Published'),
    )
    
    video_url = models.URLField(default='http://example.com/default-video-url')  # Provide a default
    slug = models.SlugField(max_length=200, unique=False) 
    status = models.CharField(choices=STATUS, max_length=100)
    is_recent = models.BooleanField(default=False)

    def __str__(self):
        return self.video_url

    def get_embed_url(self):
        import re
        youtube_id_match = re.search(r'v=([^&]+)', self.video_url)
        if youtube_id_match:
            youtube_id = youtube_id_match.group(1)
            return f'https://www.youtube.com/embed/{youtube_id}'
        return self.video_url

