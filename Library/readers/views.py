from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from .models import Readers


def readers_list(request):
    readers = Readers.objects.all()
    return render(request,'readers/readers_list.html', {'readers':readers})

def reader_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        adress = request.POST.get('adress')
        telephone = request.POST.get('telephone')
        slug = request.POST.get('slug')
        image = request.POST.get('image')
        Readers.objects.create(
            name = name,
            adress = adress,
            telephone = telephone,
            slug = slug,
            image = image,
        )
        return redirect('readers_list')
    return render(request,'readers/reader_create.html')


def reader_update(request,pk):
    readers = get_object_or_404(Readers, pk=pk)
    if request.method=='POST':
        readers.name = request.POST.get('name',readers.name) # Сохранить текущее значение, если не указано
        readers.adress = request.POST.get('adress', readers.adress)
        readers.telephone = request.POST.get('telephone',readers.telephone)
        readers.slug = request.POST.get('slug',readers.slug)
        # Проверяем, загрузили ли новое изображение
        if 'image' in request.FILES:
            readers.image = request.FILES['image']

        readers.save()
        return redirect('readers_list')
    return render(request,'readers/reader_update.html',{'readers':readers})


def reader_delete(request,pk):
    readers = get_object_or_404(Readers,pk=pk)
    if request.method == 'POST':
        readers.delete()
        return redirect('authors_list')
    return render(request,'readers/reader_delete.html',{'readers':readers})


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
