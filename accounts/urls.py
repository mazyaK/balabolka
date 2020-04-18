from django.urls import path, include
from django.contrib.auth import views as login_logout_views
from . import views as custom_views

app_name = 'accounts'
urlpatterns = [
    path('login/', login_logout_views.LoginView.as_view(), name='login'),
    path('logout/', login_logout_views.LogoutView.as_view(), name='logout'),
    path('registration/', custom_views.RegistrationView.as_view(), name='registration'),
]
