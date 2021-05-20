from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleSearchList, SaveArticleList, add_save_post, remove_save_post

app_name = 'article'

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('articles/', ArticleSearchList.as_view(), name="article_search"),
    path('saved-articles/', SaveArticleList.as_view(), name="article_save"),
    path('add-save-article/<int:pk>/', add_save_post, name="article_save_add"),
    path('remove-save-article/<int:pk>/', remove_save_post, name="article_save_remove"),
    path('articles/<int:pk>/<slug:slug>/', ArticleDetail.as_view(), name='article_detail'),
]
