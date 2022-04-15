from rest_framework import serializers

from .models import DailyTask, CompletedDailyTask


class DailyTaskDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DailyTask
        fields = '__all__'


class DailyTasklistSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DailyTask
        fields = "__all__"


class CompletedDailyTaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompletedDailyTask
        fields = '__all__'
