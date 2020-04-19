from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import redirect, render
from django.views.generic import FormView

from accounts.forms import ProfileForm, UserForm


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)



class ProfileView(FormView):
    form_class = ProfileForm
    template_name = 'accounts/profile.html'
    success_url = '/'

    @login_required
    @transaction.atomic
    def update_profile(self, request):
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Ваш профиль был успешно обновлен.')
                return redirect('accounts:profile')
            else:
                messages.error(request, 'Пожалуйста, исправьте ошибки.')
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'accounts/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
        })