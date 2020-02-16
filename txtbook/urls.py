from django.urls import path

from . import views

app_name = 'txtbook'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtextbook', views.addTextbook, name='addTextbook'),
]