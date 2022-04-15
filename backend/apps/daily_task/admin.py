from django.contrib import admin

from .models import DailyTask, CompletedDailyTask

admin.site.register(DailyTask)
admin.site.register(CompletedDailyTask)
