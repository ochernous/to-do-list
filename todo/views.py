from datetime import datetime

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    paginate_by = 4


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 4


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def undo_complete_task_view(request, pk):
    task = Task.objects.get(pk=pk)
    if not task.created_at:
        task.created_at = datetime.now()
    task.is_done = not task.is_done
    task.save()
    return redirect(reverse("todo:task-list"))
