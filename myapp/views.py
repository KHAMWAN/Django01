from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):  # ส่งโดยใช้ dictionary
    id = '001'
    name = 'John Doe'
    email = 'john@gmail.com'

    return render(request, 'index.html', {
        'id': id,
        'name': name,
        'email': email,
    })


def article(request, year, slug):
    return HttpResponse(f"Article Year: {year}, Slug: {slug}")
