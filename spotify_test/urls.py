from django.urls import path
from . import views

app_name='spotify_test'
urlpatterns = [
    path('', views.index, name='index'),
    path('backend/', views.backend, name='backend'),
    path('success/', views.success, name='success'),
    path('playlists/', views.playlists, name='playlists'),
    path('search/', views.search, name='search')
]
