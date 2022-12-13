from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from Task.models import Task
from .serializers import *


class ListDetails(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
    serializer_class = ListDetailSerializer


class ListEdit(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
    serializer_class = ListSerializer


class TaskEdit(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer