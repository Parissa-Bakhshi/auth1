import pytest

@pytest.mark.parametrize(# we can specify the data we give to this decorator,
# what outputs can have
    ("headers", "status"), #what parameters we have
    [     #values
        ({}, 415), # a blank header, status code: 415
        ({"Content-Type": "application/json"}, 401),
        ({"Content-Type": "application/json", "X-Auth-Token": "null"}, 401) 
        
    ]
)
def test_auth(client, headers, status):
    result = client.get("/api/v1/users", headers=headers)
    assert result.status_code == status 


