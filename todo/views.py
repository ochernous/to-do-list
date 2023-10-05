# from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task


class TasksListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
