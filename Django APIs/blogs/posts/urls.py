from django.urls import path, include
from .views import PostListApiView, PostDetailView, get_post_by_id

urlpatterns = [
    path('api/', PostListApiView.as_view()),
    path('api/<str:post_title>', PostDetailView.as_view()),
    path('api/post_id/<int:id>', get_post_by_id),
]
