from django.urls import path
from . import views

app_name = 'hobbies'

urlpatterns = [
    path('', views.hobby_list, name='hobby_list'),
    path('<slug:slug>/', views.hobby_detail, name='hobby_detail'),
]
