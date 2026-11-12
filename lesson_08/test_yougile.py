import os
import pytest
import requests
from dotenv import load_dotenv
from yougile_api import YougileApi

load_dotenv()

TOKEN = os.getenv("YOUGILE_TOKEN")
BASE_URL = "https://ru.yougile.com/api-v2"


@pytest.fixture
def api():
    return YougileApi(BASE_URL, TOKEN)


def test_create_project(api):
    resp = api.create_project("Мой тестовый проект")
    assert resp.status_code == 201
    assert "id" in resp.json()


def test_get_project(api):
    created = api.create_project("Проект для GET")
    project_id = created.json()["id"]
    resp = api.get_project(project_id)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Проект для GET"


def test_update_project(api):
    created = api.create_project("Проект для изменения")
    project_id = created.json()["id"]
    resp = api.update_project(project_id, {"title": "Обновленное название",
                                           "deleted": False})
    assert resp.status_code == 200


def test_create_project_no_title(api):
    resp = requests.post(f"{BASE_URL}/projects", json={}, headers=api.headers)
    assert resp.status_code == 400


def test_get_nonexistent_project(api):
    resp = api.get_project("00000000-0000-0000-0000-000000000000")
    assert resp.status_code == 404


def test_update_no_auth():
    resp = requests.put(f"{BASE_URL}/projects/123", json={"title": "Test"},
                        headers={"Content-Type": "application/json"})
    assert resp.status_code in [401, 403]
