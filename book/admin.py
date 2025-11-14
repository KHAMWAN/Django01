from django.contrib import admin
from .models import Category, Author, Book

# List_display ใช้กำหนดฟิลด์ที่จะแสดงในหน้าแอดมิน
# List_filter ใช้กำหนดฟิลด์ที่ใช้กรองข้อมูล
# Search_fields ใช้กำหนดฟิลด์ที่ใช้ค้นหาข้อมูล
# prepopulated_fields สร้าง slug จากฟิลด์ name โดยอัตโนมัติ


class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'price', 'Category', 'published']
    list_filter = ['published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
