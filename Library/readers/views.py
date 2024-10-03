from django.shortcuts import render
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from .models import Readers


def search_readers(request):
    query = request.GET.get('query', '')
    myreaders = Readers.objects.all().order_by('id')

    if query:
        myreaders = myreaders.filter(name__icontains=query)

    # Пагинация
    paginator = Paginator(myreaders,3) # 3 жанра на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'readers/readers.html', {'page_obj': page_obj, 'query': query})


def details(request, slug):
    readers = Readers.objects.get(slug=slug)
    template = loader.get_template('readers/details.html')
    context = {
        'readers': readers,
    }

    return HttpResponse(template.render(context, request))
