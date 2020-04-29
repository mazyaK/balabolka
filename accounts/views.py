from .forms import SignUpForm
from django.urls import reverse
from django.views.generic import FormView
from django.views import generic
from .models import User


class RegistrationView(FormView):
    form_class = SignUpForm
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
    template_name = 'accounts/profile_edit.html'
    fields = ['avatar', 'first_name', 'last_name', 'email', 'about_me']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'slug': self.object.slug})
