from django.urls import path
from . import views

app_name='spotify_test'
urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success')
]
