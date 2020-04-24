from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category, Comment
from .forms import CommentForm
import json


class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category_list'] = categories
        return context


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})



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

