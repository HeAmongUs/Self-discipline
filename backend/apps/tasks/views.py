from datetime import date

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TaskDetailSerializer, TasklistSerializer
from .models import Task


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


class DailyTaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TasklistSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user, completed=False)


class CompletedTaskListAPIView(generics.ListAPIView):
    serializer_class = TasklistSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # In this month
        return Task.objects.filter(
            completed=True,
        )
