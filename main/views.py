from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, \
    PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.signing import BadSignature
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView

from .forms import RegisterUserForm, AdvForm
from .models import AdvUser
from .utilities import signer


# Create your views here.
class UserPasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'main/accounts/password_change_form.html'
    success_url = reverse_lazy('main:login')

    def get_success_message(self, cleaned_data):
        return 'Вы успешно сбросили пароль'


class UserResetPassword(PasswordResetView):
    email_template_name = 'accounts/email/password_reset_email.txt'
    subject_template_name = 'accounts/email/password_reset_subject.txt'
    template_name = 'main/accounts/password_change_form.html'
    success_url = reverse_lazy('main:password_reset_done')


class UserChangePassword(SuccessMessageMixin, PasswordChangeView):
    success_url = reverse_lazy('main:profile')
    template_name = 'main/accounts/password_change_form.html'
    success_message = 'Пароль пользователя успешно изменен'


class UpdateUserInfo(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    form_class = AdvForm
    template_name = 'main/accounts/register.html'
    success_message = 'Данные пользователя были изменены %(first_name)s'
    success_url = reverse_lazy('main:profile')

    def get_object(self, queryset=None):
        return get_object_or_404(AdvUser, pk=self.request.user.pk)


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/accounts/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_active:
        template = 'main/accounts/user_is_activated.html'
    else:
        user.is_active = True
        user.save()
        template = 'main/accounts/activation_done.html'
    return render(request, template)


class RegisterNewUser(CreateView):
    model = AdvUser
    form_class = RegisterUserForm
    template_name = 'main/accounts/register.html'
    success_url = reverse_lazy('main:register_done')


# def register_new_user(request):
#     form = RegisterUserForm()
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid() and validate_passwords(form):
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1'])
#             user.is_active = False
#             form.save()
#             user_registered.send(RegisterUserForm, instance=user)
#         else:
#             return render(request, 'accounts/register.html', {'form': form})
#
#     return render(request, 'accounts/register.html', {'form': form})
#
#
# def validate_passwords(form):
#     from django.contrib.auth import password_validation
#     password1 = form.cleaned_data['password1']
#     password2 = form.cleaned_data['password2']
#     if password1 == password2:
#         password_validation.validate_password(password1)
#     else:
#         form.add_error('password2', ValidationError('Введенные пароли должны быть одинаковые'))
#     if form.errors:
#         return False
#     return True


@login_required
def profile(request):
    return render(request, 'main/accounts/profile.html')
