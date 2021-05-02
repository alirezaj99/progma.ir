from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    queryset = Article.objects.get_publish_article()
    template_name = 'article/article-list.html'
    paginate_by = 10


class ArticleSearchList(ListView):
    def get_queryset(self):
        request = self.request
        query = request.GET.get("s")
        if query is not None:
            return Article.objects.search(query)
        return Article.objects.get_publish_article()

    template_name = 'article/article-list.html'
    paginate_by = 10


class ArticleDetail(DetailView):
    # queryset = Article.objects.get_publish_article()
    def get_object(self):
        return get_object_or_404(Article.objects.get_publish_article(),
                                 slug=self.kwargs.get('slug')
                                 )

    template_name = 'article/article-detail.html'
