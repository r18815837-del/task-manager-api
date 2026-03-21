from .models import Task


def get_user_tasks(user):
    return Task.objects.filter(user=user)


def get_task_by_id(task_id):
    return Task.objects.filter(id=task_id).first()