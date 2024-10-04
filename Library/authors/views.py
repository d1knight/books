from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import loader
from django.core.paginator import Paginator
from .models import Authors


def authors_list(request):
    authors = Authors.objects.all()
    paginator = Paginator(authors, 4)  # Показать 5 авторов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'authors/authors_list.html',{'page_obj':page_obj})


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


def author_delete(request,pk):
    authors = get_object_or_404(Authors,pk=pk)
    if request.method == 'POST':
        authors.delete()
        return redirect('authors_list')
    return render(request,'authors/author_delete.html',{'authors':authors})

# Пагинация вывод на страницу
def search_authors(request):
    query = request.GET.get('query', '')
    myauthors = Authors.objects.all().order_by('id')

    if query:
        myauthors = myauthors.filter(name__icontains=query)

    # Пагинация
    paginator = Paginator(myauthors,3) # 3 жанра на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'authors/authors.html', {'page_obj': page_obj, 'query': query})

def about(request, slug):
    authors = Authors.objects.get(slug=slug).first()
    template = loader.get_template('authors/about.html')
    context = {
        'authors': authors,
    }
    return HttpResponse(template.render(context, request))
