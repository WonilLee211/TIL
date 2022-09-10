from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    title = forms.forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the title',
                'maxlength':10
            }
        ),
    )

    class Meta:
        model = Article
        fields = '__all__'
