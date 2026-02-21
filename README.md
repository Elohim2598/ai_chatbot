# AI Chatbot

A full-stack AI chatbot built with a **Flask** backend and a **SvelteKit** frontend. Conversations are powered by **Groq** (Llama 3.3 70B), authentication is handled by **Supabase**, and the UI features a dark copper-toned design with GSAP animations.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | SvelteKit + TypeScript + Tailwind CSS |
| Backend | Python + Flask |
| AI | Groq API — `llama-3.3-70b-versatile` |
| Auth | Supabase (email/password) |
| Animations | GSAP |

---

## Project Structure

```
ai_chatbot/
├── backend/
│   ├── db/
│   │   └── supabase.py          # Supabase client
│   ├── routes/
│   │   └── v1/
│   │       ├── v1.py            # Blueprint — mounts all routes at /api/v1
│   │       ├── chat.py          # POST /api/v1/chat
│   │       └── heartbeat.py     # GET  /api/v1/heartbeat
│   ├── app.py                   # Flask entry point
│   ├── groq_client.py           # Groq client
│   ├── requirements.txt
│   └── .env                     # Environment variables (not committed)
│
├── frontend/
│   ├── src/
│   │   ├── routes/
│   │   │   ├── (landing)/           # Public landing page
│   │   │   │   ├── +layout.svelte   # Dark copper background
│   │   │   │   └── +page.svelte     # Landing page
│   │   │   ├── (protected)/
│   │   │   │   └── chat/
│   │   │   │       └── +page.svelte # Main chat UI
│   │   │   ├── auth/
│   │   │   │   ├── +layout.svelte   # Shared dark background for auth pages
│   │   │   │   ├── login/           # Login form
│   │   │   │   ├── register/        # Registration form
│   │   │   │   ├── logout/          # Logout action (POST only)
│   │   │   │   └── error/           # Auth error page
│   │   │   ├── +layout.svelte
│   │   │   ├── +layout.ts
│   │   │   └── +layout.server.ts
│   │   ├── hooks.server.ts          # Supabase auth + route guard
│   │   └── app.css
│   ├── package.json
│   └── .env                         # Public env vars (not committed)
│
└── README.md
```

---

## Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- A [Supabase](https://supabase.com) project
- A [Groq](https://console.groq.com) API key

---

## Setup

### 1. Clone the repository

```bash
git clone git@github.com:Elohim2598/ai_chatbot.git
cd ai_chatbot
```

### 2. Backend

```bash
cd backend

# Create and activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate   # Windows
# source .venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key
GROQ_API_KEY=your_groq_api_key
```

Start the backend:

```bash
python app.py
# Runs at http://127.0.0.1:5000
```

Run backend tests:

```bash
python -m pytest tests/ -v
```

> **Note:** Flask does not hot-reload `.env` changes. Restart the server after editing `.env`.

### 3. Frontend

```bash
cd frontend
npm install
```

Create a `.env` file in the `frontend/` directory:

```env
PUBLIC_SUPABASE_URL=https://your-project.supabase.co
PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

Start the frontend:

```bash
npm run dev
# Runs at http://localhost:5173
```

Run frontend tests:

```bash
npm test
```

---

## API Reference

### `POST /api/v1/chat`

Send a message and receive a reply from the AI.

**Headers**

```
Authorization: Bearer <supabase_access_token>
Content-Type: application/json
```

**Request body**

```json
{
  "message": "What is the capital of France?",
  "history": [
    { "role": "user",  "parts": ["Hello!"] },
    { "role": "model", "parts": ["Hi! How can I help you?"] }
  ]
}
```

- `message` — the current user message (required)
- `history` — previous turns in the conversation (optional, pass `[]` for the first message)

**Response**

```json
{
  "reply": "The capital of France is Paris."
}
```

**Error response**

```json
{
  "error": "Unauthorized"
}
```

| Status | Meaning |
|---|---|
| `200` | Success |
| `400` | Missing `message` field |
| `401` | Missing or invalid auth token |
| `500` | Groq API error |

---

### `GET /api/v1/heartbeat`

Health check — returns `OK`.

---

## Authentication

Authentication is handled by **Supabase**. The app supports email/password sign-up and login.

| Route | Description |
|---|---|
| `/auth/register` | Create a new account |
| `/auth/login` | Log in to an existing account |
| `/auth/logout` | Sign out (form POST action) |
| `/chat` | Protected — redirects to `/auth/login` if not authenticated |

The route guard lives in `frontend/src/hooks.server.ts`. Any route inside `(protected)/` requires an active Supabase session.

---

## Environment Variables

### Backend — `backend/.env`

| Variable | Description |
|---|---|
| `SUPABASE_URL` | Your Supabase project URL |
| `SUPABASE_KEY` | Your Supabase `anon` public key |
| `GROQ_API_KEY` | Your Groq API key |

### Frontend — `frontend/.env`

| Variable | Description |
|---|---|
| `PUBLIC_SUPABASE_URL` | Your Supabase project URL |
| `PUBLIC_SUPABASE_ANON_KEY` | Your Supabase `anon` public key |

---

## Contributing

1. Fork the repository and clone your fork.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature`
5. Open a Pull Request against `main` and request a review.

Please keep pull requests focused — one feature or fix per PR.

---

## Known Limitations

- **Conversation history is not persisted** — refreshing the page clears the chat. Database persistence is a planned feature.
- **Groq free tier** — subject to rate limits (15 requests/min, 1,500/day on the free plan).
- **Single user per session** — no multi-user conversation support yet.
