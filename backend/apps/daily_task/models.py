from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from taggit.managers import TaggableManager

from datetime import date


User = get_user_model()


class DailyTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    streak = models.IntegerField(validators=[MinValueValidator(0), ])
    order = models.IntegerField(validators=[MinValueValidator(1), ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f'{self.title} | {self.user.username}'


class CompletedDailyTask(models.Model):
    value = models.BooleanField(default=False)
    date = models.DateField(default=date.today)
    daily_task = models.ForeignKey(DailyTask, on_delete=models.CASCADE)

    class Meta:
        unique_together = 'date', 'daily_task'

    def __str__(self):
        return f'{self.daily_task.title} | {self.daily_task.user.username} | {self.date}'

