#from django.shortcuts import render
"""
    ListView : List the images on the homeoage
    CreateView : extend and upload a new images
"""
from django.views.generic import ListView, CreateView

"""
    reverse_lazy : handle the redirect back to our homepage after submitting the form
"""
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    
    
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
