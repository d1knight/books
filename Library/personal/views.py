from django.shortcuts import render
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse

from .models import Personal


'''
def genres(request):
    data = {
        'title': 'Жанры'
    }
    return render(request, 'genres/genres.html', data)
'''
def search_personal(request):
    query = request.GET.get('query', '')
    mypersonal = Personal.objects.all().order_by('id')

    if query:
        mypersonal = mypersonal.filter(name__icontains=query)

    # Пагинация
    paginator = Paginator(mypersonal,3) # 3 жанра на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'personal/personal.html', {'page_obj': page_obj, 'query': query})


def about(request, slug):
    personal = Personal.objects.get(slug=slug)
    template = loader.get_template('personal/about.html')
    context = {
        'personal': personal,
    }

    return HttpResponse(template.render(context, request))

'''


def showPersonal(request):
    mypersonal = Personal.objects.all()
    template = loader.get_template('personal/personal.html')
    data = {
        'title': 'Персонал',
        'mypersonal': mypersonal,
    }

    return HttpResponse(template.render(data, request))
'''