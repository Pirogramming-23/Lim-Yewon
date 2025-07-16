from django.urls import path
from .views import *
urlpatterns = [
	    path('', views_main),
        path('<int:pk>/', ideas_read),
        path('create/', ideas_create),
        path('<int:pk>/delete/', ideas_delete),
        path('<int:pk>/update/', ideas_update),
        path('devtools/', devtools_list),
]