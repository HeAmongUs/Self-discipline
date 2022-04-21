from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DailyTaskDetailSerializer, DailyTasklistSerializer, CompletedDailyTaskListSerializer
from .models import DailyTask, CompletedDailyTask


class DailyTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DailyTaskDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return DailyTask.objects.filter(user=user)


class DailyTaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DailyTasklistSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return DailyTask.objects.filter(user=user)

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = DailyTasklistSerializer(queryset, many=True)

        today = date.today()
        user = self.request.user
        completed_list = CompletedDailyTask.objects.filter(value=True, daily_task__user=user, date=today)
        list_with_completed_task_order = []
        for completed in completed_list:
            list_with_completed_task_order.append(completed.daily_task.order)
        for task in serializer.data:
            if task["order"] in list_with_completed_task_order:
                task["completed"] = True
            else:
                task["completed"] = False

        return Response(serializer.data)


class CompletedDailyTaskListAPIView(generics.ListAPIView):
    serializer_class = CompletedDailyTaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # In this month
        return CompletedDailyTask.objects.filter(
            value=True,
            date__month=date.today().month,
            date__year=date.today().year,
            date__day__gte=1
        )


class CreateOrUpdateCompletedDailyTaskAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        # Create or update CompletedDailyTask today instance
        user = request.user
        daily_task = DailyTask.objects.get(user=user, id=request.data["daily_task"])
        try:
            completed_daily_task = CompletedDailyTask.objects.get(daily_task=daily_task, date=date.today())
        except ObjectDoesNotExist:
            completed_daily_task = None
        if completed_daily_task is not None:
            completed_daily_task.value = request.data["value"]
        else:
            completed_daily_task = CompletedDailyTask.objects.create(
                daily_task=daily_task,
                value=request.data["value"],
            )
        completed_daily_task.save()
        return Response({"success": "Success"})
