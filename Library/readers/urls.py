from django.urls import path
from . import views

urlpatterns = [
    path('readers/', views.search_readers, name='search_readers'),
    path('readers/details/<slug:slug>', views.details, name='readers_page'),
]

