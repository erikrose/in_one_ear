from django.forms import ModelForm, TextInput

from blog.models import Article


class ArticleForm(ModelForm):
    class Meta(object):
        model = Article
        exclude = ('slug',)
        widgets = {
            'title': TextInput
        }
