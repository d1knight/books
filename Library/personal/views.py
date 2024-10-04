from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse

from .models import Personal


def personal_list(request):
    personal = Personal.objects.all()
    paginator = Paginator(personal, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'personal/personal_list.html', {'page_obj':page_obj})

def personal_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        photo = request.POST.get('photo')
        adress = request.POST.get('adress')
        slug = request.POST.get('slug')

        Personal.objects.create(
            name=name,
            position=position,
            photo=photo,
            adress=adress,
            slug=slug,
        )
        return redirect('personal_list')
    return render(request,'personal/personal_create.html')


def personal_update(request,pk):
    personal = get_object_or_404(Personal,pk=pk)
    if request.method=='POST':
        personal.name = request.POST.get('name',personal.name)
        personal.position = request.POST.get('position',personal.position)
        personal.adress = request.POST.get('adress',personal.adress)

        if 'photo' in request.FILES:
            personal.photo = request.FILES['photo']

        personal.save()
        return redirect('personal_list')
    return render(request,'personal/personal_update.html', {'personal':personal})


def personal_delete(request,pk):
    personal = get_object_or_404(Personal,pk=pk)
    if request.method == 'POST':
        personal.delete()
        return redirect('personal_list')
    
    return render(request,'personal/personal_delete.html', {'personal':personal})





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