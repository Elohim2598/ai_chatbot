import sys
import os
from unittest.mock import MagicMock

# Add backend root to sys.path so imports resolve correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ── Mock external dependencies BEFORE importing the Flask app ─────────────────
# Without this, module-level code in app.py (load_dotenv, supabase client,
# groq client) would run and fail in CI / environments without .env files.

# Mock dotenv so load_dotenv() is a no-op
mock_dotenv = MagicMock()
mock_dotenv.load_dotenv.return_value = True
sys.modules["dotenv"] = mock_dotenv

# Build shared mock objects — tests import these via fixtures below
mock_supabase = MagicMock()
mock_groq = MagicMock()

# Patch db.supabase so "from db.supabase import supabase" gives our mock
mock_db_supabase_module = MagicMock()
mock_db_supabase_module.supabase = mock_supabase
sys.modules["db"] = MagicMock()
sys.modules["db.supabase"] = mock_db_supabase_module

# Patch groq_client so "from groq_client import client" gives our mock
mock_groq_client_module = MagicMock()
mock_groq_client_module.client = mock_groq
sys.modules["groq_client"] = mock_groq_client_module

# ── Now import the app (all external deps are already mocked) ─────────────────
import pytest  # noqa: E402
from app import app as flask_app  # noqa: E402

flask_app.config["TESTING"] = True


@pytest.fixture(scope="session")
def app():
    return flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def supabase_mock():
    """Returns the shared Supabase mock, reset before each test."""
    mock_supabase.reset_mock()
    return mock_supabase


@pytest.fixture
def groq_mock():
    """Returns the shared Groq mock, reset before each test."""
    mock_groq.reset_mock()
    return mock_groq
