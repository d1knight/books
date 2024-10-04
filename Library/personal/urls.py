from django.urls import path
from . import views

urlpatterns = [
    path('personal/', views.search_personal, name='search_personal'),
    path('personal/about/<slug:slug>', views.about, name='personal_page'),
    path('personal/list/',views.personal_list, name='personal_list'),
    path('personal/list/create/', views.personal_create, name='personal_create'),
    path('personal/list/update/<int:pk>', views.personal_update, name='personal_update'),
    path('personal/list/delete/<int:pk>', views.personal_delete, name='personal_delete'),
]
