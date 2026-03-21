from .models import Task


def create_task(user, title, description=""):
    return Task.objects.create(
        user=user,
        title=title,
        description=description
    )


def update_task(task, **data):
    for field, value in data.items():
        setattr(task, field, value)
    task.save()
    return task


def delete_task(task):
    task.delete()