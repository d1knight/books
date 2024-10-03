from django.urls import path
from . import views

urlpatterns = [
    # path('Books/', views.ShowBooks, name='Books'),
    path('Books/', views.search_books, name='search_books'),
    path('Books/', views.books_list, name='books_list'),
    path('Books/details/<slug:slug>/', views.details, name='details_page'),
    path('Books/list/',views.bookList,name='book_list'),
    path('Books/list/create/',views.book_create,name='book_create'),
    path('Books/list/update/<int:pk>/',views.book_update,name='book_update'),
    path('Books/list/delete/<int:pk>/',views.book_delete,name='book_delete'),
]
