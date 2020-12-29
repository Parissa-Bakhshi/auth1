import pytest

@pytest.mark.parametrize(
    ("headers", "json", "status"),
    [
        ({"Content-type": "application/json"}, {"username": "test7", "password": "test7"}, 201),
        ({"Content-type": "application/json"}, {"username": "test", "password": "test"}, 409),
        ({"Content-type": "application/json"}, {}, 400),
        ({"Content-type": "application/json"}, {"username": "", "password": ""}, 400) 

    ]
)
def test_create_user(client, headers, json, status):
    result = client.post("/api/v1/users", json=json, headers=headers)
    assert result.status_code == status

