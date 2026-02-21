"""
Unit tests for build_messages() in routes/v1/chat.py.

This is a pure function with no external dependencies, so no mocking needed.
"""
from routes.v1.chat import build_messages


def test_no_history_appends_user_message():
    result = build_messages([], "Hello")
    assert result == [{"role": "user", "content": "Hello"}]


def test_user_turn_preserved():
    history = [{"role": "user", "parts": ["Hi there"]}]
    result = build_messages(history, "Follow up")
    assert result[0] == {"role": "user", "content": "Hi there"}
    assert result[-1] == {"role": "user", "content": "Follow up"}


def test_model_role_converted_to_assistant():
    history = [
        {"role": "user", "parts": ["Hi"]},
        {"role": "model", "parts": ["Hello!"]},
    ]
    result = build_messages(history, "Next message")
    assert result[1] == {"role": "assistant", "content": "Hello!"}


def test_multi_turn_conversation():
    history = [
        {"role": "user", "parts": ["What is 2+2?"]},
        {"role": "model", "parts": ["4"]},
        {"role": "user", "parts": ["And 3+3?"]},
        {"role": "model", "parts": ["6"]},
    ]
    result = build_messages(history, "Thanks")
    assert len(result) == 5
    assert result[1]["role"] == "assistant"
    assert result[3]["role"] == "assistant"
    assert result[-1] == {"role": "user", "content": "Thanks"}


def test_missing_parts_key_defaults_to_empty_string():
    # If "parts" key is absent, the default [""] is used → content is ""
    history = [{"role": "user"}]
    result = build_messages(history, "Hello")
    assert result[0] == {"role": "user", "content": ""}


def test_message_is_always_last():
    history = [
        {"role": "user", "parts": ["First"]},
        {"role": "model", "parts": ["Second"]},
    ]
    result = build_messages(history, "Current message")
    assert result[-1]["role"] == "user"
    assert result[-1]["content"] == "Current message"
