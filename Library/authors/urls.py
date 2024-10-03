from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('authors/', views.search_authors, name='search_authors'),
    path('authors/about/<slug:slug>', views.about, name='about_page'),
    path('authors/list/', views.authors_list, name='authors_list'),
    path('authors/list/create/', views.author_create, name='author_create'),
    path('authors/list/update/<int:pk>', views.author_update, name='author_update'),
    path('authors/list/delete/<int:pk>', views.author_delete, name='author_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # путь статистическийга проектке