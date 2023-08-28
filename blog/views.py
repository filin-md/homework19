from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('blog:list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('blog:list')

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')
