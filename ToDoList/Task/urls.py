from django.urls import path
from Task.views import *


urlpatterns = [
    path('lists/', ListDetails.as_view(), name='first'),
    path('list/<int:pk>/', ListEdit.as_view(), name='AddList'),
    path('task/<int:pk>/', TaskEdit.as_view()),
    path('add-task/', TaskDetail.as_view())
]
