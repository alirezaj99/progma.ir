from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleSearchList

app_name = 'article'

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('articles/', ArticleSearchList.as_view(), name="article_search"),
    path('articles/<slug:slug>/', ArticleDetail.as_view(), name='article_detail'),
]
