from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.search_bookings, name = 'search_bookings'),
    path('bookings/about/<slug:slug>', views.about, name='booking_page')
]