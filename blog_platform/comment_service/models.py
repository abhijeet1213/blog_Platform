
# Create your models here.
from django.db import models
from django.conf import settings

from blog_service.models import Blog


class Comment(models.Model):
    objects = None
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Comment by {self.author} on {self.blog}'
