from django.urls import path
from . import views

# Patrón de url
urlpatterns = [
    path('', views.post_list, name='post_list'),
]