from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = [field.name for field in Post._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('name', 'date', 'on_list')
    list_filter = 'name'
    search_fields = ('name', 'category__name') # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.unregister(Post) # разрегистрируем наши товары
