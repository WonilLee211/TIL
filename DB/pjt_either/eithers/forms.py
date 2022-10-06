from django import forms
from .models import Either, Comment
class EitherForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'my-title w-100',
                'maxlength':30,
            }
        )
        )
    issue_a = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'my-title w-100',
                'maxlength':30,
            }
        )
        )
    issue_b = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'my-title w-100',
                'maxlength':30,
            }
        )
        )
    class Meta:
        model = Either
        fields = '__all__'

class CommentForm(forms.ModelForm):
    CHOICES = (
        ('issue_a', "BlUE"),
        ('issue_b', "RED"),
    )
    pick = forms.CharField(
        widget = forms.Select(
            choices=CHOICES,
            attrs={
                'class':'w-100',
                'maxlength':7,
            }
        )
    )
    content = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'my-title w-100',
                'maxlength':30,
                'placeholder':'Content',
            }
        )
    )
    class Meta:
        model = Comment
        exclude = ('either',)