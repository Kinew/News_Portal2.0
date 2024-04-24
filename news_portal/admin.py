from django.contrib import admin
from .models import *
from modeltranslation.admin import \
    TranslationAdmin  # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)


# Register your models here.

# Регистрируем модели для перевода в админке

class CategoryAdmin(TranslationAdmin):
    model = Category


class MyModelAdmin(TranslationAdmin):
    model = MyModel


def nullfy_quantity(modeladmin, request,
                    queryset):  # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)


nullfy_quantity.short_description = 'Обнулить товары'  # описание для более понятного представления в админ панеле задаётся, как будто это объект


# создаём новый класс для представления товаров в админке
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'on_stock', 'quantity')
    list_filter = ('post', 'quantity', 'name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category__name')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(News)
admin.site.register(MyModel)
# Register your models here.