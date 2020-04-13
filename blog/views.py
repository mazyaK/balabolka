from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Post, Category
import json


class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category_list'] = categories
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class FilteredListsView(generic.ListView):
    template_name = 'blog/category.html'
    queryset = Post.objects.filter(status=1).order_by('created_on')

    def get_context_data(self, **kwargs):
        context = super(FilteredListsView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category_list'] = categories
        context['posts'] = Post.objects.filter(status=1, category=Category.objects.get(
            name=self.kwargs['category_name'])).order_by('created_on')
        return context

