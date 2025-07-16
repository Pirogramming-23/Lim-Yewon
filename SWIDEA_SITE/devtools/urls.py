from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
    path('', devtools_list),
    path('<int:pk>/', devtools_read),
    path('create/', devtools_create),
    path('<int:pk>/delete/', devtools_delete),
    path('<int:pk>/update/', devtools_update),
]