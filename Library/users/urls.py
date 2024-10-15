from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('admin/', views.admin_list, name='admin_list'),
    path('registr/', views.register, name='registr'),
    path('login/', views.admin_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('books/',views.books_list, name='books_list'),
    path('books/create/',views.book_create, name='books_create'),
    path('books/update/<int:pk>/',views.book_update, name='books_update'),
    path('books/delete/<int:pk>/',views.book_delete, name='books_delete'),
    path('authors/',views.authors_list, name='authors_list'),
    path('authors/create/',views.author_create, name='author_create'),
    path('authors/update/<int:pk>/',views.author_update, name='author_update'),
    path('authors/delete/<int:pk>/',views.author_delete, name='author_delete'),
    path('', views.admin_view, name='default'),  # Путь по умолчанию
    
]
