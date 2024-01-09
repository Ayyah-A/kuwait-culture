from django.urls import path

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
]
