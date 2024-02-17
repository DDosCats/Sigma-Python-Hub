from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.index, name= 'index'),
    path('<int:post_id>/', views.post,name='post'),
    path('create/', views.create, name = 'create'),

]