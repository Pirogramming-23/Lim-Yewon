from django.urls import path
from .views import *

app_name = 'sites'

urlpatterns = [
	    path('', views_main),
        path('<int:pk>/', ideas_read),
        path('create/', ideas_create),
        path('<int:pk>/delete/', ideas_delete),
        path('<int:pk>/update/', ideas_update),
        path('<int:pk>/star-toggle/', toggle_star, name='toggle_star'),
        path('<int:pk>/interest/<str:action>/', change_interest, name='change_interest'),
]