from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User
from apps.tasks.models import Task


class UserAuthTaskFlowTests(APITestCase):
    def test_user_can_register(self):
        url = "/api/users/register/"
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "StrongPass123",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, "testuser")

    def test_user_can_login_and_get_tokens(self):
        User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="StrongPass123",
        )

        url = "/api/login/"
        data = {
            "username": "testuser",
            "password": "StrongPass123",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_authenticated_user_can_create_task(self):
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="StrongPass123",
        )

        self.client.force_authenticate(user=user)

        url = "/api/tasks/"
        data = {
            "title": "Test task",
            "description": "Test description",
            "status": "todo",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().user, user)

    def test_user_sees_only_own_tasks(self):
        user1 = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="StrongPass123",
        )
        user2 = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="StrongPass123",
        )

        Task.objects.create(
            title="Task 1",
            description="Only user1 task",
            status="todo",
            user=user1,
        )
        Task.objects.create(
            title="Task 2",
            description="Only user2 task",
            status="done",
            user=user2,
        )

        self.client.force_authenticate(user=user1)

        response = self.client.get("/api/tasks/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Task 1")

    def test_unauthorized_user_cannot_create_task(self):
        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Hack task",
                "description": "Should not be created",
                "status": "todo",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Task.objects.count(), 0)

    def test_user_cannot_view_other_users_task_by_id(self):
        user1 = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="StrongPass123",
        )
        user2 = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="StrongPass123",
        )

        other_task = Task.objects.create(
            title="Private task",
            description="Belongs to user2",
            status="todo",
            user=user2,
        )

        self.client.force_authenticate(user=user1)

        response = self.client.get(f"/api/tasks/{other_task.id}/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_tasks_by_status_works_correctly(self):
        user = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="StrongPass123",
        )

        Task.objects.create(
            title="Todo task",
            description="todo",
            status="todo",
            user=user,
        )
        Task.objects.create(
            title="Done task",
            description="done",
            status="done",
            user=user,
        )

        self.client.force_authenticate(user=user)

        response = self.client.get("/api/tasks/?status=done")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Done task")
        self.assertEqual(response.data["results"][0]["status"], "done")