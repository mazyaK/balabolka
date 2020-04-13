from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<str:category_name>/search/', views.FilteredListsView.as_view(), name='filtered_post')
]