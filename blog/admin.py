from django.contrib import admin
from django.contrib.admin import ModelAdmin

from in_one_ear.blog.models import Article, Comment


class ArticleAdmin(ModelAdmin):
    pass


class CommentAdmin(ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
