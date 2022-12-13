from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from Task.models import Task
from .serializers import *


class ListDetails(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListDetailSerializer
    #authentication_classes = (BasicAuthentication,)

    def get_queryset(self):
        return List.objects.filter(user__id=self.request.user.id)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ListEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    #authentication_classes = (BasicAuthentication, SessionAuthentication)
    queryset = List.objects.all()
    serializer_class = ListSerializer


class TaskEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer


class TaskDetail(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskEditSerializer
    #authentication_classes = (BasicAuthentication,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
