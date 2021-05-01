from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    queryset = Article.objects.get_publish_article()
    template_name = 'article/article-list.html'
    paginate_by = 6


class ArticleDetail(DetailView):
    queryset = Article.objects.get_publish_article()
    template_name = 'article/article-detail.html'
