from django.urls import path

from .views import DailyTaskDetailView, DailyTaskListCreateAPIView, CompletedDailyTaskListAPIView, \
    CreateOrUpdateCompletedDailyTaskAPIView

urlpatterns = [
    path('<int:pk>/', DailyTaskDetailView.as_view()),
    path('complete/<int:pk>/', CreateOrUpdateCompletedDailyTaskAPIView.as_view()),
    path('completed/', CompletedDailyTaskListAPIView.as_view()),
    path('', DailyTaskListCreateAPIView.as_view()),
]
