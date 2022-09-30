from django.contrib import admin
from django.urls import path
from . import views

app_name = "movie_crud"
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name="new"),
    path('create/', views.create, name='create'),
    path('delete/<int:re_pk>', views.delete, name='delete'),
    path('detail/<int:re_pk>', views.detail, name='detail'),
    path('edit/<int:re_pk>', views.edit, name="edit"),
    path('recreate/<int:re_pk>', views.recreate, name='recreate')
]
