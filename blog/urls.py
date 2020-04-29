from django.urls import path
from . import views



app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/change/post_new/', views.post_new, name='post_new'),
    path('<str:category_name>/search/', views.FilteredListsView.as_view(), name='filtered_post'),
]