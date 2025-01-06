
# Create your views here.
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        return Comment.objects.filter(blog_id=post_id)


class RegisterView:
    @classmethod
    def as_view(cls):
        pass


class LoginView:
    @classmethod
    def as_view(cls):
        pass