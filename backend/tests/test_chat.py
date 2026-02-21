"""
Tests for POST /api/v1/chat

Uses monkeypatch to patch `routes.v1.chat.supabase` and `routes.v1.chat.client`
directly — this gives each test a fresh, isolated mock with no bleed-over.
"""
from unittest.mock import MagicMock


def _supabase_ok():
    """Fresh Supabase mock that passes auth (get_user returns a truthy user)."""
    mock = MagicMock()
    mock.auth.get_user.return_value.user = MagicMock(id="user-123")
    return mock


def _supabase_bad_token():
    """Fresh Supabase mock that raises on get_user (simulates invalid JWT)."""
    mock = MagicMock()
    mock.auth.get_user.side_effect = Exception("invalid JWT")
    return mock


def _groq_ok(reply="Test reply."):
    """Fresh Groq mock that returns a specific reply."""
    mock = MagicMock()
    mock.chat.completions.create.return_value.choices[0].message.content = reply
    return mock


def _groq_error():
    """Fresh Groq mock that raises on completions.create."""
    mock = MagicMock()
    mock.chat.completions.create.side_effect = Exception("Groq API unavailable")
    return mock


# ── Authorization ──────────────────────────────────────────────────────────────

def test_no_auth_header_returns_401(client):
    res = client.post("/api/v1/chat", json={"message": "hello"})
    assert res.status_code == 401
    assert res.json["error"] == "Unauthorized"


def test_wrong_auth_scheme_returns_401(client):
    res = client.post(
        "/api/v1/chat",
        json={"message": "hello"},
        headers={"Authorization": "Basic abc123"},
    )
    assert res.status_code == 401


def test_invalid_token_returns_401(client, monkeypatch):
    monkeypatch.setattr("routes.v1.chat.supabase", _supabase_bad_token())
    res = client.post(
        "/api/v1/chat",
        json={"message": "hello"},
        headers={"Authorization": "Bearer bad_token"},
    )
    assert res.status_code == 401


# ── Input validation ───────────────────────────────────────────────────────────

def test_missing_message_returns_400(client, monkeypatch):
    monkeypatch.setattr("routes.v1.chat.supabase", _supabase_ok())
    res = client.post(
        "/api/v1/chat",
        json={},
        headers={"Authorization": "Bearer valid_token"},
    )
    assert res.status_code == 400
    assert res.json["error"] == "message is required"


def test_whitespace_only_message_returns_400(client, monkeypatch):
    monkeypatch.setattr("routes.v1.chat.supabase", _supabase_ok())
    res = client.post(
        "/api/v1/chat",
        json={"message": "   "},
        headers={"Authorization": "Bearer valid_token"},
    )
    assert res.status_code == 400


def test_no_json_body_returns_400(client, monkeypatch):
    monkeypatch.setattr("routes.v1.chat.supabase", _supabase_ok())
    res = client.post(
        "/api/v1/chat",
        headers={"Authorization": "Bearer valid_token"},
    )
    assert res.status_code == 400


# ── Successful chat ────────────────────────────────────────────────────────────

def test_successful_chat_returns_reply(client, monkeypatch):
    monkeypatch.setattr("routes.v1.chat.supabase", _supabase_ok())
    monkeypatch.setattr("routes.v1.chat.client", _groq_ok("Paris."))

    res = client.post(
        "/api/v1/chat",
        json={"message": "What is the capital of France?", "history": []},
        headers={"Authorization": "Bearer valid_token"},
    )

    assert res.status_code == 200
    assert res.json["reply"] == "Paris."


def test_chat_with_history_converts_model_to_assistant(client, monkeypatch):
    groq = _groq_ok("Yes.")
    monkeypatch.setattr("routes.v1.chat.supabase", _supabase_ok())
    monkeypatch.setattr("routes.v1.chat.client", groq)

    history = [
        {"role": "user", "parts": ["What is 2+2?"]},
        {"role": "model", "parts": ["4"]},
    ]
    res = client.post(
        "/api/v1/chat",
        json={"message": "Are you sure?", "history": history},
        headers={"Authorization": "Bearer valid_token"},
    )

    assert res.status_code == 200

    # Verify Groq received correctly formatted messages
    call_kwargs = groq.chat.completions.create.call_args.kwargs
    messages = call_kwargs["messages"]
    assert messages[1]["role"] == "assistant"  # "model" → "assistant"
    assert messages[-1] == {"role": "user", "content": "Are you sure?"}


# ── Groq errors ────────────────────────────────────────────────────────────────

def test_groq_error_returns_500(client, monkeypatch):
    monkeypatch.setattr("routes.v1.chat.supabase", _supabase_ok())
    monkeypatch.setattr("routes.v1.chat.client", _groq_error())

    res = client.post(
        "/api/v1/chat",
        json={"message": "hello"},
        headers={"Authorization": "Bearer valid_token"},
    )

    assert res.status_code == 500
    assert "error" in res.json
