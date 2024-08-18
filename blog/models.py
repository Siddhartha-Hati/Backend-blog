from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import validate_image_size
from django.utils import timezone

class Post(models.Model):
    BLOG = 'blog'
    REVIEW = 'review'
    CATEGORY_CHOICES = [
        (BLOG, 'Blog Post'),
        (REVIEW, 'Review Post'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', 
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png','gif']), validate_image_size], 
        null=True, 
        blank=True
    )
    created_date = models.DateTimeField(blank=True, null=True)  # Allow blank and null
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=BLOG,
    )

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title