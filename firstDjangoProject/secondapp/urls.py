from django.urls import path, include

from secondapp import views

urlpatterns = [
    path('', views.home, name='second-app home'),
    path('about/', views.about, name='second-app about'),
]
