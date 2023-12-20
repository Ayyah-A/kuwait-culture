from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('mohe/', views.mohe, name='mohe'),
    path('kuwait_university/', views.kuwait_university, name='kuwait_university'),
]
