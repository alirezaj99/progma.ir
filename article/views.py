from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article
from account.models import User


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
    template_name = 'article/article-detail.html'

    def get_object(self):
        article = get_object_or_404(Article.objects.get_publish_article(),
                                    slug=self.kwargs.get('slug')
                                    )
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)
        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

# subject = 'welcome to progma'
#      message = f'Hi {self.request.user.username}, thank you for registering in {self.object.title}.'
#      email_from = settings.EMAIL_HOST_USER
#      recipient_list = [self.request.user.email, ]
#      send_mail(subject, message, email_from, recipient_list)
