from django.urls import path
from . import urls

app_name='eithers'
urlpatterns = [
    path('index', urls.index, name='index'),
]