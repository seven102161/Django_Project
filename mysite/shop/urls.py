from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.detail, name='detail'),
    path('<str:name>/result/', views.result, name='result'),
    path('<str:name>/buy/', views.buy, name='buy'),
]