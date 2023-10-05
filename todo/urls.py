from django.urls import path

from todo.views import TasksListView, TagsListView


urlpatterns = [
    path("", TasksListView.as_view(), name="task-list"),
    path("tags/", TagsListView.as_view(), name="tags"),
]

app_name = "todo"
