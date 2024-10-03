from django.http import HttpResponse
from django.template import loader

from django.template.loader import render_to_string
from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Books
from authors.models import Authors
from genres.models import Genres
from django.db.models import Q


# def ShowBooks(request):
#   mybooks = Books.objects.all()
#   template = loader.get_template('books/books.html')
#   context = {
#     'mybooks': mybooks,
#   }
#   return HttpResponse(template.render(context, request))


def bookList(request):
    books = Books.objects.all()

    paginator = Paginator(books,15) # 5 книг на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'Books/book_list.html',{'page_obj':books})

#Добавление книги

from django.shortcuts import render, redirect
from .models import Books
from authors.models import Authors
from genres.models import Genres

def book_create(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        count = request.POST.get('count')
        authors_ids = request.POST.getlist('authors')  # Получаем id авторов
        genres_ids = request.POST.getlist('genres')    # Получаем id жанров
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        publishingYear = request.POST.get('publishingYear')
        price = request.POST.get('price')
        publication = request.POST.get('publication')
        binding = request.POST.get('binding')

        # Создаём книгу без связи с авторами и жанрами
        book = Books.objects.create(
            name=name,
            count=count,
            slug=slug,
            description=description,
            publishingYear=publishingYear,
            price=price,
            publication=publication,
            binding=binding
        )

        # Добавляем связи с авторами и жанрами
        authors = Authors.objects.filter(id__in=authors_ids)
        genres = Genres.objects.filter(id__in=genres_ids)
        
        book.authors.add(*authors)  # Используем add() для ManyToMany
        book.genres.add(*genres)    # Используем add() для ManyToMany

        # Устанавливаем связи
        book.authors.set(authors)
        book.genres.set(genres)

        return redirect('book_list')
    
    # Получаем всех авторов и жанры для выбора в форме
    all_authors = Authors.objects.all()
    all_genres = Genres.objects.all()

    # Отображаем форму создания книги
    return render(request, 'Books/book_create.html', {
        'authors': all_authors,
        'genres': all_genres
    })


def book_update(request, pk):
    books = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        books.name = request.POST.get('name',books.name)
        books.count = request.POST.get('count',books.count)
        authors_ids = request.POST.getlist('authors')  # Получаем id авторов
        genres_ids = request.POST.getlist('genres')    # Получаем id жанров
        books.slug = request.POST.get('slug',books.slug)
        books.description = request.POST.get('description',books.description)
        books.publishingYear = request.POST.get('publishingYear',books.publishingYear)
        books.price = request.POST.get('price',books.price)
        books.publication = request.POST.get('publication',books.publication)
        books.binding = request.POST.get('binding',books.binding)

        # Обновляем связь ManyToManyField для авторов и жанров
        authors = Authors.objects.filter(id__in=authors_ids)
        genres = Genres.objects.filter(id__in=genres_ids)
        books.authors.set(authors)
        books.genres.set(genres)

        books.save()
        return redirect('book_list')

    # Передаем всех авторов и жанры для редактирования
    all_authors = Authors.objects.all()
    all_genres = Genres.objects.all()

    return render(request, 'Books/book_update.html', {
        'books': books,
        'authors': all_authors,
        'genres': all_genres
    })

def book_delete(request,pk):
    books = get_object_or_404(Books,pk=pk)
    if request.method=='POST':
        books.delete()
        return redirect('book_list')
    return render(request,'Books/book_delete.html',{'books':books})

def search_books(request):
    query = request.GET.get('query', '')
    mybooks = Books.objects.all().order_by('id')

    if query:
        mybooks = mybooks.filter(
            Q(name__icontains=query)| Q(authors__name__icontains=query)
            )

    # Пагинация
    paginator = Paginator(mybooks,3) # 5 книг на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/books.html', {'page_obj': page_obj, 'query': query})

def books_list(request):
    side_books = Books.objects.all() # Получаем все книги из базы данных
    genre = request.GET.get('genre') # Получаем значение категории из GET-запроса

    if genre:
        side_books = side_books.filter(genre=genre)   # Фильтруем по жанрам

    return render(request,'books/books.html',{'side_books':side_books})

def details(request, slug):
    books = Books.objects.get(slug=slug)
    template = loader.get_template('Books/details.html')
    context = {
        'books': books,
    }

    return HttpResponse(template.render(context, request))

