from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='main_page'),
    path('', views.books_list, name='main_page')
]
