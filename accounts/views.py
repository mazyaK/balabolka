from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.views import generic
from .models import User


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)

class ProfileView(generic.DetailView):
    model = User
    template_name = 'accounts/profile.html'



class ProfileUpdateView(generic.UpdateView):
    model = User
    template_name= 'accounts/profile_edit.html'
    fields = ['avatar', 'first_name', 'last_name', 'email', 'about_me']

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'slug': self.object.slug})



