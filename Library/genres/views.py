from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse

from .models import Genres




def genres_list(request):
    genres = Genres.objects.all()
    paginator = Paginator(genres, 4)  # Показать 4 жанров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'genres/genres_list.html', {'page_obj': page_obj})

def genre_create(request):
    if request.method=='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        slug = request.POST.get('slug')
        Genres.objects.create(
            name=name,
            description=description,
            slug=slug,
        )
        return redirect('genres_list')
    return render(request,'genres/genre_create.html')

def genre_update(request,pk):     #Функция обновления жанров    02/10/2024
    genres = get_object_or_404(Genres,pk=pk)
    if request.method=='POST':
        genres.name = request.POST.get('name',genres.name)
        genres.description = request.POST.get('description',genres.description)
        genres.slug = request.POST.get('slug',genres.slug)
        genres.save()
        return redirect('genres_list')
    
    return render(request,'genres/genre_update.html',{'genres':genres})


def genre_delete(request, pk):
    genres = get_object_or_404(Genres,pk=pk)
    if request.method == 'POST':
        genres.delete()
        return redirect('genres_list')
    
    return render(request,'genres/genre_delete.html',{'genres':genres})


def search_genres(request):
    query = request.GET.get('query', '')
    mygenres = Genres.objects.all().order_by('id')

    if query:
        mygenres = mygenres.filter(name__icontains=query)

    # Пагинация
    paginator = Paginator(mygenres,3) # 3 жанра на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'genres/genres.html', {'page_obj': page_obj, 'query': query})


def about(request, slug):
    genres = Genres.objects.get(slug=slug)
    template = loader.get_template('genres/about.html')
    context = {
        'genres': genres,
    }

    return HttpResponse(template.render(context, request))