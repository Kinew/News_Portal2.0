from django.urls import path
from news_portal import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('news/', cache_page(60)(views.NewsList.as_view())),
    path('<int:pk>', cache_page(300)(views.News.as_view()), name ='post_detail'),
    path('news/create/', cache_page(300)(views.PostCreate.as_view()), name='news_create'),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('articles/create/', views.PostCreate.as_view(), name='articles_create'),
    path('<int:pk>/edit/', views.PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('index/', views.Index.as_view(), name='index'),
]