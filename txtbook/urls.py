from django.urls import path

from . import views

app_name = 'txtbook'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtextbook', views.addTextbook, name='addTextbook'),
    # path('allposts', views.allPosts, name='allPosts'),
    path('allposts', views.allPostsView.as_view(), name='allPosts'),
    path('<int:pk>/', views.PostView.as_view(), name='post'),
]