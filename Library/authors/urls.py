from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('authors/', views.search_authors, name='search_authors'),
    path('authors/about/<slug:slug>/', views.about, name='about_page'),
    path('authors/list/', views.authors_list, name='authors_list'),
    path('authors/list/create/', views.author_create, name='author_create'),
    path('authors/list/update/<int:pk>/', views.author_update, name='author_update'),
    path('authors/list/delete/<int:pk>/', views.author_delete, name='author_delete'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login_view, name='login'),    # Маршрут для авторизации и регистрации
    # path('logout/',views.logout_view, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
