from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include("apps.accounts.urls")),
    path('api/v1/daily_task/', include("apps.daily_task.urls")),
    path('api/v1/task/', include("apps.tasks.urls")),
]
