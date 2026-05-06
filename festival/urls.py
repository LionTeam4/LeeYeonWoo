from django.urls import path
from .views import *

app_name= 'festival'

urlpatterns = [
    path('', InfoListView.as_view()),
    path('<int:pk>/',InfoDetailView.as_view()),
    path('reviews/', ReviewView.as_view()),
    path('post', PostListView.as_view()),
    path('post/<int:pk>/',PostDetailView.as_view()),
    path('post/comments/', CommentView.as_view()),
]