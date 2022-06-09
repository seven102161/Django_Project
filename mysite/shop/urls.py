from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:name>', views.detail, name='detail'),
]