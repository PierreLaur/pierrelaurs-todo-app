from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("update/<int:task_id>/", views.update_task, name="update_task"),
    path("complete/<int:task_id>/", views.complete_task, name="complete_task"),
    path("create/", views.create_task, name="create_task"),  # Add this line
]
