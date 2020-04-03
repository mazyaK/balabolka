from django.shortcuts import render
from django.views import generic
from .models import Post, Category


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'blog/index.html'


class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'blog/category.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
