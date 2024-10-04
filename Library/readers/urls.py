from django.urls import path
from . import views

urlpatterns = [
    path('readers/', views.search_readers, name='search_readers'),
    path('readers/list/',views.readers_list, name='readers_list'),
    path('readers/list/create/', views.reader_create, name='reader_create'),
    path('readers/list/update/<int:pk>', views.reader_update, name='reader_update'),
    path('readers/list/delete/<int:pk>', views.reader_delete, name='reader_delete'),
    path('readers/details/<slug:slug>', views.details, name='readers_page'),

]

