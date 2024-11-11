from django.urls import path
from .views import (IndexView, ShowTaskView, CreateTaskView, UpdateTaskView,
                    DeleteTaskView)


urlpatterns = [
    path('', IndexView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='tasks_create'),
    path('<int:pk>', ShowTaskView.as_view(), name='tasks_show'),
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='tasks_update'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='tasks_delete'),
]
