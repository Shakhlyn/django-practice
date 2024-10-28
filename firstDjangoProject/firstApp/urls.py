from django.urls import path

from firstApp import views

urlpatterns = [
    # http://localhost:8001/first-app
    path('', views.home, name='first app home'),

    # http://localhost:8001/first-app/about
    path('about/', views.about, name='first-app about'),
    path("books/", views.all_books, name="books"),
    # path("books/<int:pk>", views.book_detail, name="book_detail"),
    path("books/<int:book_id>", views.book_detail, name="book_detail"),

]
