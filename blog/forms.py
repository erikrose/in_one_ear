from django.forms import ModelForm, TextInput

from in_one_ear.blog.models import Article, Comment


class ArticleForm(ModelForm):
    class Meta(object):
        model = Article
        exclude = ('slug',)
        widgets = {
            'title': TextInput
        }


class CommentForm(ModelForm):
    class Meta(object):
        model = Comment
        fields = ('body',)
