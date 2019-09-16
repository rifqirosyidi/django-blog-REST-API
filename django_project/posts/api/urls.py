from django.urls import path, include
from .views import PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView

app_name = 'api-posts'
urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    # path('create/', views.post_create, name='create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
]
