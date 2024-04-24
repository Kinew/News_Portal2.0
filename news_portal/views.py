from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime
from django.utils import timezone
import pytz #  импортируем стандартный модуль для работы с часовыми поясами

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect, render, get_object_or_404
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.core.cache import cache
from django.utils.translation import gettext as _ # импортируем функцию для перевода
# from django.utils.translation import activate, get_supported_language_variant, LANGUAGE_SESSION_KEY
from .models import MyModel

from .models import *
from .forms import PostForm
from .filters import PostFilter

from rest_framework import viewsets
from rest_framework import permissions

from education.serializers import *
from education.models import *

from django.http import HttpResponse
# from django.http.response import HttpResponse #  импортируем респонс для проверки текста
from django.views import View
import logging

logger = logging.getLogger(__name__)


class NewsList(ListView):
    model = Post
    ordering = '-dateCreations'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 2
# Create your views here.


    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


 # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class News(DetailView):
    template_name = 'sample_app/post_detail.html'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'post-{self.kwargs["pk"]}',
                        None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
            return obj


# Добавляем новое представление для создания товаров.
class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news_portal.add_post',)
    raise_exception = True
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_create.html'
    context_object_name = 'create'


    def form_valid(self, form):
        post = form.save(commit = False)
        if self.request.path == '/articles/create/':
            post.post_news = 'AR'
        return super().form_valid(form)



# Добавляем представление для изменения товара.
class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news_portal.update_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news_portal.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CategoryListView(ListView):
    model = Post
    template_name = 'name/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id= self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


# Create your views here

class Index(View):

    def get(self, request):
        context = {
            'models': MyModel.objects.all(),
            'current_time': timezone.localtime(timezone.now()),
            'timezones': pytz.common_timezones
        }

        return render(request, 'index.html', context)

class NewsViewset(viewsets.ModelViewSet):
   queryset = News.objects.all()
   serializer_class = NewsSerializer


class ArticlesViewset(viewsets.ModelViewSet):
   queryset = Articles.objects.all()
   serializer_class = ArticlesSerializer