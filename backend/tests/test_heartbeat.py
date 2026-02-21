"""
Tests for GET /api/v1/heartbeat
"""


def test_heartbeat_returns_200(client):
    res = client.get("/api/v1/heartbeat")
    assert res.status_code == 200


def test_heartbeat_returns_ok(client):
    res = client.get("/api/v1/heartbeat")
    assert res.data == b"OK"
