from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('',views.index, name= 'index'),
    path('contact/', views.contacts, name = 'contact'),
    path('about/', views.about, name='about'),
    path('navig/',views.navig, name = 'navigat'),
]