from django.shortcuts import render,redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Booking
from personal.models import Personal
from readers.models import Readers
from Books.models import Books
from django.template import loader
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.text import slugify
from django.urls import reverse

def booking_list(request):
    booking = Booking.objects.all()
    return render(request,'bookings/booking_list.html',{'booking':booking})

def booking_create(request):
    if request.method == 'POST':
        personal_id = request.POST.get('personal')
        readers_id = request.POST.get('readers')
        books_id = request.POST.get('books')
        get_date = request.POST.get('getDate')
        return_date = request.POST.get('returnDate')

        # Получение объектов из базы данных по выбранным ID
        personal = Personal.objects.get(id=personal_id)
        readers = Readers.objects.get(id=readers_id)
        books = Books.objects.get(id=books_id)

        # Создание нового заказа
        booking = Booking.objects.create(
            personal=personal,
            readers=readers,
            books=books,
            getDate=get_date,
            returnDate=return_date,
            slug=slugify(f'{readers.name}-{books.name}-{get_date}')
        )
        
        # После успешного создания заказа перенаправляем на список заказов
        return redirect(reverse('booking_list'))

    # Если запрос GET — отображаем форму
    else:
        personal = Personal.objects.all()
        readers = Readers.objects.all()
        books = Books.objects.all()

        context = {
            'personal': personal,
            'readers': readers,
            'books': books,
        }
        
        return render(request, 'bookings/booking_create.html', context)
    

def booking_update(request, pk):
    # Получаем существующее бронирование по ID
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST':
        personal_id = request.POST.get('personal')
        readers_id = request.POST.get('readers')
        books_id = request.POST.get('books')
        get_date = request.POST.get('getDate')
        return_date = request.POST.get('returnDate')

        # Обновляем объекты в базе данных по выбранным ID
        booking.personal = Personal.objects.get(id=personal_id)
        booking.readers = Readers.objects.get(id=readers_id)
        booking.books = Books.objects.get(id=books_id)
        booking.getDate = get_date
        booking.returnDate = return_date
        booking.slug = slugify(f'{booking.readers.name}-{booking.books.name}-{get_date}')

        # Сохраняем изменения
        booking.save()

        # Перенаправление на список бронирований
        return redirect(reverse('booking_list'))

    else:
        personal = Personal.objects.all()
        readers = Readers.objects.all()
        books = Books.objects.all()

        context = {
            'booking': booking,
            'personal': personal,
            'readers': readers,
            'books': books,
        }
        
        return render(request, 'bookings/booking_update.html', context)

def booking_delete(request, pk):
    # Получаем бронирование по ID
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST':
        # Удаляем бронирование
        booking.delete()
        # Перенаправляем на список бронирований
        return redirect(reverse('booking_list'))

    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})


def search_bookings(request):
    query = request.GET.get('query', '')
    mybookings = Booking.objects.all().order_by('id')

    if query:
        mybookings = mybookings.filter(
        Q(books__name__icontains=query) | Q(personal__name__icontains=query)| Q(readers__name__icontains=query)
)


    # Пагинация
    paginator = Paginator(mybookings,4) # 5 заказов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'bookings/bookings.html', {'page_obj': page_obj, 'query': query})


def about(request, slug):
    bookings = Booking.objects.get(slug=slug)
    template = loader.get_template('bookings/about.html')
    context = {
        'bookings': bookings,
    }

    return HttpResponse(template.render(context, request))

