from django.urls import path

from theme_soft_design import views as t_views
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('mohe/', views.mohe, name='mohe'),
    path('kuwait_university/', views.kuwait_university, name='kuwait_university'),
    path('civil_service/', views.civil_service, name='civil_service'),
    path('kuwait_authority/', views.kuwait_authority, name='kuwait_authority'),
    path('paaet/', views.paaet, name='paaet'),
    path('announcements/', views.announcements, name='announcements'),
    path('students/', views.students, name='students'),
    path('students/documents', views.documents, name='documents'),
    path('positions/', views.positions, name='positions'),



##Authentication
    path('account/login/', views.UserLoginView.as_view(), name='employee_login'),

    path('accounts/register/', t_views.register, name='register'),
    path('accounts/logout/', t_views.logout_view, name='logout'),
    path('accounts/password-change/', t_views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
    path('accounts/password-reset/', t_views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/',
         views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
