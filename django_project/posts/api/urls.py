from django.urls import path, include
from .views import PostListAPIView, PostDetailAPIView

app_name = 'api-posts'
urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    # path('create/', views.post_create, name='create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    # path('<slug:slug>/update/', views.post_update),
    # path('<slug:slug>/delete/', views.post_delete),
]
