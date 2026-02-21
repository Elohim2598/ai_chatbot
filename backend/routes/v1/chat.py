from flask import request, jsonify
from .v1 import v1
from db.supabase import supabase
from groq_client import client


def get_current_user():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return None
    token = auth_header[len("Bearer "):]
    try:
        response = supabase.auth.get_user(token)
        return response.user
    except Exception:
        return None


def build_messages(history, message):
    messages = []
    for item in history:
        role = item.get("role")
        text = item.get("parts", [""])[0]
        # Groq uses "assistant" instead of "model"
        if role == "model":
            role = "assistant"
        messages.append({"role": role, "content": text})
    messages.append({"role": "user", "content": message})
    return messages


@v1.route('/chat', methods=['POST'])
def chat():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    body = request.get_json(silent=True) or {}
    message = body.get("message", "").strip()
    history = body.get("history", [])

    if not message:
        return jsonify({"error": "message is required"}), 400

    try:
        messages = build_messages(history, message)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
        )
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        print(f"Groq error: {e}")
        return jsonify({"error": str(e)}), 500
