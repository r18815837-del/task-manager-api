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
async def test_create_project(client):
    headers = await register_and_login(client, "proj@example.com", "projuser")

    response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "My Project",
            "description": "First project",
        },
        headers=headers,
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "My Project"
    assert data["description"] == "First project"
    assert "id" in data
    assert "owner_id" in data


@pytest.mark.asyncio
async def test_get_my_projects(client):
    headers = await register_and_login(client, "proj2@example.com", "projuser2")

    await client.post(
        "/api/v1/projects/",
        json={
            "name": "Project A",
            "description": "Desc A",
        },
        headers=headers,
    )

    response = await client.get(
        "/api/v1/projects/",
        headers=headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["name"] == "Project A"