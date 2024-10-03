from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Booking
from django.template import loader
from django.core.paginator import Paginator
from django.db.models import Q



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

