from django.conf import settings
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete
from django.urls import path

from .views import register, profile, profile_edit, avatar_edit, password_change, email_change, email_change_confirm

app_name = 'User'
urlpatterns = [
    path('login', login, {'template_name': 'Auth/login.html', }, name='login'),
    path('logout', logout, {'template_name': 'Auth/logout.html', }, name='logout'),
    path('password-change', password_change, name='password_change'),
    path('password-reset', password_reset, {
        'template_name': 'Auth/password_reset.html',
        'email_template_name': 'Auth/email/password_reset_email.html',
        'subject_template_name': 'Auth/email/password_reset_subject.txt',
        'post_reset_redirect': 'User:password_reset_done',
        'from_email': getattr(settings, 'EMAIL_FROM'),
    }, name='password_reset'),
    path('password-reset-done', password_reset_done,
         {'template_name': 'Auth/password_reset_done.html', },
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', password_reset_confirm, {
        'template_name': 'Auth/password_reset_confirm.html',
        'post_reset_redirect': 'User:password_reset_complete',
    }, name='password_reset_confirm'),
    path('password-reset-complete', password_reset_complete,
         {'template_name': 'Auth/password_reset_complete.html', },
         name='password_reset_complete'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('email-change', email_change, name='email_change'),
    path('email-change-confirm/<token>', email_change_confirm, name="email_change_confirm"),
    path('profile-edit', profile_edit, name='profile_edit'),
    path('avatar-edit', avatar_edit, name='avatar_edit'),
]