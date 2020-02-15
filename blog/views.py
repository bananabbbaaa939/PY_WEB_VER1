from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post

class PostCV(CreateView):
    model = Post

class PostUV(UpdateView):
    model = Post
class PostRV(DeleteView):
    model = Post
