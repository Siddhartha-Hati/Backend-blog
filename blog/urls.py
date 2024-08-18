from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, ReviewPostViewSet

router = DefaultRouter()
router.register(r'blogpost', BlogPostViewSet, basename='blogpost')
router.register(r'reviewpost', ReviewPostViewSet, basename='reviewpost')

urlpatterns = [
    path('', include(router.urls)),
]