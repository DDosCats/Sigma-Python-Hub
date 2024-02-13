from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.index, name= 'index'),
    path('magazine/', views.magazine, name = 'magazine'),
    path('about/', views.about, name= 'about')
]