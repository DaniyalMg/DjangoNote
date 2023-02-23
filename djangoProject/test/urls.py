from django.urls import path

from . import views

urlpatterns = [
    path('getnote/', views.getnote, name='getnote'),
    path('note/', views.note, name='note'),
]
