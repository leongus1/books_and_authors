from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors/', views.author_index),
    path('books/<int:id_num>/', views.book_list),
    path('authors/<int:id_num>/', views.authors_list),
    path('books/add/', views.add_book),
    path('authors/add/', views.add_author),
    path('books/<int:id_num>/add/', views.book_add_auth),
    path('authors/<int:id_num>/add/', views.auth_add_book),
]