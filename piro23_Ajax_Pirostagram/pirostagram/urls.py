from django.urls import path
from .views import *

app_name = 'pirostagram'

urlpatterns = [
    path('', posts_list, name='Plist'),
    path('<int:pk>/', posts_detail, name='detail'),
    path('like_ajax/', like_ajax, name='like_ajax'),
    path("<int:post_id>/comments/", comments_create, name='comments_create'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]