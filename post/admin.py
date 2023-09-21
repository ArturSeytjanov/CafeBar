from django.contrib import admin
from .models import Post
from .models import Category
from .models import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name']
    ordering = ['-id']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
