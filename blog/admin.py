from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_date', 'published_date')
    list_filter = ('category', 'created_date', 'published_date')
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'image', 'category', 'created_date', 'published_date')
admin.site.register(Post, PostAdmin)