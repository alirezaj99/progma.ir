from django.contrib import admin
from .models import Article, ArticleTag, IPAddress, SaveArticle,Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'author_str',
                    'slug',
                    'tags_str',
                    'status',
                    'send_email',
                    ]
    list_filter = ['status', 'publish', ]
    list_editable = ['status']

    class meat:
        model = Article


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'slug',
                    'active',
                    ]
    list_filter = ['active', 'created', ]
    list_editable = ['active']

    class meat:
        model = ArticleTag


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(IPAddress)
admin.site.register(SaveArticle)
admin.site.register(Comment)
