from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'


class PostByCategory(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        posts = Post.objects.filter(categoty__slug=category_slug)
        return posts


