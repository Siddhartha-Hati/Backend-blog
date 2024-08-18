from rest_framework import viewsets, filters
from .models import Post
from .serializers import PostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_date', 'published_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', Post.BLOG)  
        queryset = queryset.filter(category=category)
        return queryset
class ReviewPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_date', 'published_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', Post.REVIEW)  # Default to 'blog'
        queryset = queryset.filter(category=category)
        return queryset