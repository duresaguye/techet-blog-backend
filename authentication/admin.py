from django.contrib import admin
from .models import *


# Register your models here.
class TagTublerInline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines =[TagTublerInline]
    list_display = ['title','author','date','status','section','main_post']
    list_editable =['status','section','main_post']
    search_fields = ['title','author','section']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
