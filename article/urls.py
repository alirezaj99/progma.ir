from django.urls import path
from .views import ArticleList

app_name = 'article'

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list')
]
