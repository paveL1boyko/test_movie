from django.contrib.auth.views import LogoutView, PasswordResetDoneView, LoginView
from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'main'

urlpatterns = [
    path('register/activate/<str:sign>', user_activate, name='register_activate'),
    path('register/done', TemplateView.as_view(template_name='main/accounts/register_done.html'), name='register_done'),
    path('register/', RegisterNewUser.as_view(), name='register'),
    path('password/reset_done', PasswordResetDoneView.as_view(template_name='main/accounts/password_rest_done.html'),
         name='password_reset_done'),
    path('profile/change', UpdateUserInfo.as_view(), name='profile_change'),
    path('password/reset', UserResetPassword.as_view(), name='reset_password'),
    path('password/reset/confirm/<uidb64>/<token>/', UserPasswordResetConfirm.as_view(), name='confirm_reset_password'),
    path('password/change', UserChangePassword.as_view(), name='password_change'),
    path('login/', LoginView.as_view(template_name='main/accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='main/accounts/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
]
