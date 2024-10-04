from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.search_bookings, name = 'search_bookings'),
    path('bookings/about/<slug:slug>', views.about, name='booking_page'),
    path('bookings/list/', views.booking_list, name='booking_list'),
    path('bookings/list/create/', views.booking_create, name='booking_create'),
    path('bookings/list/update/<int:pk>', views.booking_update, name='booking_update'),
    path('bookings/list/delete/<int:pk>', views.booking_delete, name='booking_delete'),
]