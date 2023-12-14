from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # template url
    path('', views.index, name='index'),
    
    # apis
    path('books/', views.get_all_books),
    path('books/add/', views.add_book),
    path('books/get/', views.get_book),
    path('books/update/', views.update_book),
    path('books/delete/', views.delete_book),
    
    # video
    path('process_video/', views.process_video),
    
    
]
