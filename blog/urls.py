from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(ArticleListView.as_view()), name='blog'),
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('view/<slug:slug>/', ArticleDetailView.as_view(), name='view_article'),
    path('edit/<slug:slug>/', ArticleUpdateView.as_view(), name='edit_article'),
    path('delete/<slug:slug>/', ArticleDeleteView.as_view(), name='delete_article'),
]
