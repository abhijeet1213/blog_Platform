from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
# Create your views here.
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from django.template.loader import get_template
from django.http import HttpResponse

def blog_list(request, blogs=None):

    blogs = ["Blog 1", "Blog 2", "Blog 3"]
    return render(request, 'blog_list.html', {'blogs': blogs})

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_detail.html', {'blog': blog})

def about(request, ):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Save the blog post to the database
        Blog.objects.create(title=title, content=content)

        # Redirect to the blog list or another page
        return redirect('blog_list')

    return render(request, 'create_post.html')

class RegisterView:
    pass


class LoginView:
    pass