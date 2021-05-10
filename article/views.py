from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, DetailView
from .models import Article, SaveArticle, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.views.generic.edit import FormMixin


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


class SaveArticleList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        save_article = SaveArticle.objects.get(user=self.request.user)
        articles = save_article.articles.get_publish_article().order_by('-article_savearticle_articles.id')
        return articles

    template_name = 'article/save-article-list.html'
    paginate_by = 10


class ArticleDetail(FormMixin, DetailView):
    # queryset = Article.objects.get_publish_article()
    template_name = 'article/article-detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article:article_detail', kwargs={'slug': self.object.slug})

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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'دیدگاه تو با موفقیت ثبت شد ، منتظر تایید باش', 'success')
            return self.form_valid(form)
        else:
            messages.error(request, 'یه مشکلی هست دوباره سعی کن !', 'danger')
            return self.form_invalid(form)

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            self.obj = form.save(commit=False)
            self.obj.article = self.object
            self.obj.user = self.request.user
            self.obj.status = False
            try:
                # id integer e.g. 15
                self.obj.parent_id = int(self.request.POST.get('parent_id'))
            except:
                self.obj.parent_id = None

            form.save()
        return super(ArticleDetail, self).form_valid(form)


@login_required()
def add_save_post(request, **kwargs):
    if request.method == 'POST':
        article_pk = kwargs['pk']
        save_article = SaveArticle.objects.get(user=request.user)
        article = Article.objects.get(pk=article_pk)
        if article is None or article.status == 'd':
            raise Http404()
        if article in save_article.articles.get_publish_article():
            messages.error(request, 'این مقاله رو قبلا ذخیره کردی', 'danger')
            if request.GET.get("next"):
                return redirect(request.GET.get("next"))
            else:
                return HttpResponseRedirect(reverse('article:article_list'))
        save_article.articles.add(article)
        messages.success(request, 'مقاله با موفقیت ذخیره شد', 'success')
        save_article.save()
        if request.GET.get("next"):
            return redirect(request.GET.get("next"))
        else:
            return HttpResponseRedirect(reverse('article:article_list'))
    else:
        raise Http404('404 error')


@login_required()
def remove_save_post(request, **kwargs):
    if request.method == 'POST':
        article_pk = kwargs['pk']
        save_article = SaveArticle.objects.get(user=request.user)
        article = Article.objects.get(pk=article_pk)
        if article is None or article.status == 'd':
            raise Http404()
        if article not in save_article.articles.get_publish_article():
            messages.error(request, 'اصا این مقاله رو ذخیره نکردی !', 'danger')
            if request.GET.get("next"):
                return redirect(request.GET.get("next"))
            else:
                return HttpResponseRedirect(reverse('article:article_list'))
        save_article.articles.remove(article)
        messages.success(request, 'مقاله با موفقیت از ذخیره ها حذف شد', 'success')
        save_article.save()
        if request.GET.get("next"):
            return redirect(request.GET.get("next"))
        else:
            return HttpResponseRedirect(reverse('article:article_list'))
    else:
        raise Http404('404 error')
