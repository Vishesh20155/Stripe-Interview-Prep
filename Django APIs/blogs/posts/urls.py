from django.urls import path, include
from .views import PostListApiView, PostDetailView

urlpatterns = [
    path('api/', PostListApiView.as_view()),
    path('api/<str:post_title>', PostDetailView.as_view()),
]
