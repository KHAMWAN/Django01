from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # name ใช้ตั้งชื่อในการอ้างอิง URL
    re_path(
        r'article/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$', views.article, name='article'),
]
