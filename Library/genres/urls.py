from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.search_genres, name = 'search_genres'),
    path('genres/about/<slug:slug>', views.about, name='genre_page'),
    path('genres/list/',views.genres_list, name="genres_list"),
    path('genres/list/create',views.genre_create, name="genre_create"),
    path('genres/list/update/<int:pk>',views.genre_update, name="genre_update"),
    path('genres/list/delete/<int:pk>',views.genre_delete, name="genre_delete"),
]
