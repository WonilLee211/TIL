from django.urls import path
from . import views

app_name='eithers'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:either_id>/', views.detail, name='detail'),
    path('create_comment/<int:either_id>/', views.create_comment, name='create_comment'),
]