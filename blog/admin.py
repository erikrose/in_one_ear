from django.contrib import admin
from django.contrib.admin import ModelAdmin, site

from blog.models import Article


class ArticleAdmin(ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
