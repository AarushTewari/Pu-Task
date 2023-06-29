from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-creation_date']

class BlogDetailView(DetailView):
    model = Post
    template_name =  'blog_details.html'

class AddBlogView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdateBlogView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html' 

class DeleteBlogView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def login(request):
    return render(request, 'login.html')