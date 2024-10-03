from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.search_personal, name='search_personal'),
    path('personal/about/<slug:slug>', views.about, name='personal_page'),
]
