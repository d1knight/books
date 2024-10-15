from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout,login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from authors.models import Authors
from Books.models import Books
from genres.models import Genres
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')
            return redirect('users:login')  # Перенаправьте на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})




# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})

def admin_list(request):
    return render(request,'users/adm.html')

def admin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Используем alias auth_login
            return redirect('users:admin_list')
        else:
            messages.error(request, "Неправильное имя пользователя или пароль.")

    return render(request, 'users/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main_page')  # Исправлено на 'users:admin'
    return redirect('home_page')  # Исправлено на 'users:login'


@login_required
def authors_list(request):
    authors = Authors.objects.all()
    paginator = Paginator(authors, 4)  # Показать 5 авторов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'authors/authors_list.html',{'page_obj':page_obj})



@login_required
def author_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        slug = request.POST.get('slug')
        banner = request.POST.get('banner')
        Authors.objects.create(
            name=name,
            description=description,
            slug=slug,
            banner=banner,
        )
        return redirect('authors_list')
    return render(request,'authors/author_create.html')

@login_required
def author_update(request,pk):
    authors = get_object_or_404(Authors, pk=pk)
    if request.method=='POST':
        authors.name = request.POST.get('name',authors.name) # Сохранить текущее значение, если не указано
        authors.description = request.POST.get('description', authors.description)
        authors.slug = request.POST.get('slug',authors.slug)
        # Проверяем, загрузили ли новое изображение
        if 'banner' in request.FILES:
            authors.banner = request.FILES['banner']

        authors.save()
        return redirect('authors_list')
    return render(request,'authors/author_update.html',{'authors':authors})


@login_required
def author_delete(request,pk):
    authors = get_object_or_404(Authors,pk=pk)
    if request.method == 'POST':
        authors.delete()
        return redirect('authors_list')
    return render(request,'authors/author_delete.html',{'authors':authors})


@login_required
def books_list(request):
    books = Books.objects.all()

    paginator = Paginator(books,3) # 4 книг на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'users/books/book_list.html',{'page_obj':page_obj})

@login_required
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

        return redirect('users:books_list')
    
    # Получаем всех авторов и жанры для выбора в форме
    all_authors = Authors.objects.all()
    all_genres = Genres.objects.all()

    # Отображаем форму создания книги
    return render(request, 'users/books/book_create.html', {
        'authors': all_authors,
        'genres': all_genres
    })


@login_required
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
        return redirect('users:books_list')

    # Передаем всех авторов и жанры для редактирования
    all_authors = Authors.objects.all()
    all_genres = Genres.objects.all()

    return render(request, 'users/books/book_update.html', {
        'books': books,
        'authors': all_authors,
        'genres': all_genres
    })


@login_required
def book_delete(request,pk):
    books = get_object_or_404(Books,pk=pk)
    if request.method=='POST':
        books.delete()
        return redirect('users:book_list')
    return render(request,'users/books/book_delete.html',{'books':books})


@login_required
def authors_list(request):
    authors = Authors.objects.all()
    paginator = Paginator(authors, 3)  # Показать 3 авторов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'users/authors/authors_list.html',{'page_obj':page_obj})


@login_required
def author_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        slug = request.POST.get('slug')
        banner = request.POST.get('banner')
        Authors.objects.create(
            name=name,
            description=description,
            slug=slug,
            banner=banner,
        )
        return redirect('users:authors_list')
    return render(request,'users/authors/author_create.html')


@login_required
def author_update(request,pk):
    authors = get_object_or_404(Authors, pk=pk)
    if request.method=='POST':
        authors.name = request.POST.get('name',authors.name) # Сохранить текущее значение, если не указано
        authors.description = request.POST.get('description', authors.description)
        authors.slug = request.POST.get('slug',authors.slug)
        # Проверяем, загрузили ли новое изображение
        if 'banner' in request.FILES:
            authors.banner = request.FILES['banner']

        authors.save()
        return redirect('users:authors_list')
    return render(request,'users/authors/author_update.html',{'authors':authors})



@login_required
def author_delete(request,pk):
    authors = get_object_or_404(Authors,pk=pk)
    if request.method == 'POST':
        authors.delete()
        return redirect('users:authors_list')
    return render(request,'users/authors/author_delete.html',{'authors':authors})


