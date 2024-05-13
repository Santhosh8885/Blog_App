from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import (
    BlogPostListCreateAPIView,
    BlogPostDetailAPIView,
    BlogPostListAPIView,
    BlogPostSearchAPIView,
)

urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(), name='user_registration'),
    path('login/', obtain_auth_token, name='user_login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='user_logout'),
    path('posts/', BlogPostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetailAPIView.as_view(), name='post-detail'),
    path('posts/search/', BlogPostSearchAPIView.as_view(), name='post-search'),
    path('posts/all/', BlogPostListAPIView.as_view(), name='post-list'),
]

