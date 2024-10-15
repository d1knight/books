from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.main, name='main_page'),
    path('', views.books_list, name='main_page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main_page'), name='logout'),
]
