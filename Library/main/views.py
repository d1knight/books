from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from Books.models import Books  # Импортируем модель Books
from authors.models import Authors
from django.core.paginator import Paginator  # Импортируем Paginator

# def main(request):
#     data = {
#         'title': 'Главная страница'
#     }
#     return render(request, 'main/main.html', data)



def books_list(request):
    side_books = Books.objects.all().order_by('name')
    all_authors = Authors.objects.all()  # Получаем всех авторов для выпадающего списка
    genres = request.GET.getlist('genres')  # Получаем список выбранных жанров
    authors = request.GET.getlist('authors')  # Получаем список выбранных авторов
    bindings = request.GET.getlist('bindings') # Получаем список выбранных переплетов

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if genres:
        side_books = side_books.filter(genres__name__in=genres)  # Фильтруем по жанрам

    if authors:
        side_books = side_books.filter(authors__name__in=authors)  # Фильтруем по авторам
    
# Фильтруем по минимальной и максимальной цене
    if min_price:
        try:
            side_books = side_books.filter(price__gte=float(min_price))
        except (ValueError, TypeError):
            pass  # Игнорируем, если преобразование не удалось

    if max_price:
        try:
            side_books = side_books.filter(price__lte=float(max_price))
        except (ValueError, TypeError):
            pass  # Игнорируем, если преобразование не удалось

# Фильтруем по переплетам
    if bindings:
        side_books = side_books.filter(binding__in=bindings)
    
    unique_bindings = Books.objects.values_list('binding', flat=True).distinct()

    paginator = Paginator(side_books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'main/main.html', {
        'page_obj': page_obj,
        'selected_authors': authors,  # Передаем выбранных авторов
        'genres': genres,  # Передаем выбранные жанры
        'authors': all_authors,
        'min_price': min_price,
        'max_price': max_price,
        'binding': bindings, 
        'unique_bindings': unique_bindings,
    })

