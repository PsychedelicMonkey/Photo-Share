from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('photo/<int:pk>/', views.detail, name='photo-detail'),
]
