from django.urls import path

from todo.views import TasksListView


urlpatterns = [
    path("", TasksListView.as_view(), name="task-list"),
]

app_name = "todo"
