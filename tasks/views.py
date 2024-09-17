from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.views.decorators.cache import never_cache


@never_cache
def task_list(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, "task_list.html", {"tasks": tasks})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        if "name" in request.POST:
            task.name = request.POST.get("name")
        if "priority" in request.POST:
            task.priority = request.POST.get("priority")
        task.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.completed = request.POST.get("completed") == "true"
        task.save()
        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"})


def create_task(request):
    if request.method == "POST":
        if "name" in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                new_task = form.save()
                return JsonResponse(
                    {
                        "status": "success",
                        "name": new_task.name,
                        "task_id": new_task.id,
                        "priority": new_task.priority,
                    }
                )
            else:
                return JsonResponse({"status": "error", "errors": form.errors})
        return JsonResponse({"status": "error"})
    else:
        form = TaskForm()

    return render(request, "task_list.html", {"form": form})
