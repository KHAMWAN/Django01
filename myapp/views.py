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


def home(request):  # ส่งโดยใช้ dictionary

    activities = [
        'Football',
        'Running',
        'Badminton',
    ]

    return render(request, 'home.html', {
        'activities': activities,
    })


def article(request, year, slug):
    if year and slug:  # กรณีมีการส่งค่ามา
        return render(request, 'article.html', {
            'year': year,
            'slug': slug,
        })
    else:  # กรณีไม่มีการส่งค่ามา
        return render(request, 'index.html')
