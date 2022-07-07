from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from taggit.managers import TaggableManager


User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(blank=True, default=False)
    order = models.IntegerField(validators=[MinValueValidator(1), ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f'Task {self.title} | {self.user.username}'
