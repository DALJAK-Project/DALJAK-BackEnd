from django.urls import path
from . import views
from posts.views import *

urlpatterns = [
    path('post/', views.WritePostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/<int:pk>', CommentDetail.as_view()),
]