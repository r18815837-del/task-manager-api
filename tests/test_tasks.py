import pytest


async def register_and_login(client, email: str, username: str, password: str = "12345678"):
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "username": username,
            "password": password,
        },
    )

    login_response = await client.post(
        "/api/v1/auth/login",
        data={
            "username": username,
            "password": password,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.mark.asyncio
async def test_create_task(client):
    headers = await register_and_login(client, "task@example.com", "taskuser")

    project_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Task Project",
            "description": "Project for tasks",
        },
        headers=headers,
    )
    project_id = project_response.json()["id"]

    response = await client.post(
        "/api/v1/tasks/",
        json={
            "title": "My Task",
            "description": "Task description",
            "status": "todo",
            "project_id": project_id,
            "assignee_id": None,
        },
        headers=headers,
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "My Task"
    assert data["status"] == "todo"
    assert data["project_id"] == project_id


@pytest.mark.asyncio
async def test_filter_tasks_by_status(client):
    headers = await register_and_login(client, "filter@example.com", "filteruser")

    project_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Filter Project",
            "description": "Filter test",
        },
        headers=headers,
    )
    project_id = project_response.json()["id"]

    await client.post(
        "/api/v1/tasks/",
        json={
            "title": "Task Todo",
            "description": "Todo task",
            "status": "todo",
            "project_id": project_id,
            "assignee_id": None,
        },
        headers=headers,
    )

    await client.post(
        "/api/v1/tasks/",
        json={
            "title": "Task Done",
            "description": "Done task",
            "status": "done",
            "project_id": project_id,
            "assignee_id": None,
        },
        headers=headers,
    )

    response = await client.get(
        f"/api/v1/tasks/?project_id={project_id}&status=todo",
        headers=headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Task Todo"
    assert data[0]["status"] == "todo"