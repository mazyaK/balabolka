from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


