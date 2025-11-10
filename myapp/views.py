from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    id = '001'  # กำหนดข้อมูลใส่ตัวแปร
    name = 'John Doe'
    email = 'john@gmail.com'

    return render(request, 'index.html', {  # ส่งเป็น dictionary
        'id': id,
        'name': name,
        'email': email,
    })


def home(request):

    activities = [  # ใส่ Array
        'Football',
        'Running',
        'Badminton',
    ]

    return render(request, 'home.html', {  # ส่งเป็น dictionary
        'activities': activities,
    })


def article(request, year, slug):
    if year and slug:
        return render(request, 'article.html', {  # ส่งเป็น dictionary
            'year': year,
            'slug': slug,
        })
    else:  # กรณีไม่มีการส่งค่ามา
        return render(request, 'index.html')
