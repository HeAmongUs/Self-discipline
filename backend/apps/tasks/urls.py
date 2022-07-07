from django.urls import path

from .views import TaskDetailView, DailyTaskListCreateAPIView, CompletedTaskListAPIView


urlpatterns = [
    path('<int:pk>/', TaskDetailView.as_view()),
    path('completed/', CompletedTaskListAPIView.as_view()),
    path('', DailyTaskListCreateAPIView.as_view()),
]
