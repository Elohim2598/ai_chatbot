# Frontend

SvelteKit + TypeScript + Tailwind CSS frontend for the AI Chatbot.

## Stack

- [SvelteKit](https://kit.svelte.dev/) — framework
- [TypeScript](https://www.typescriptlang.org/) — type safety
- [Tailwind CSS](https://tailwindcss.com/) — styling
- [GSAP](https://gsap.com/) — animations
- [Supabase SSR](https://supabase.com/docs/guides/auth/server-side/sveltekit) — auth
- [svelte-forms-lib](https://github.com/tjinauyeung/svelte-forms-lib) + [yup](https://github.com/jquense/yup) — form validation

## Setup

```bash
npm install
```

Create `frontend/.env`:

```env
PUBLIC_SUPABASE_URL=https://your-project.supabase.co
PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

## Commands

| Command           | Description                                 |
| ----------------- | ------------------------------------------- |
| `npm run dev`     | Start dev server at `http://localhost:5173` |
| `npm run build`   | Build for production                        |
| `npm run preview` | Preview production build                    |
| `npm run check`   | Type-check with `svelte-check`              |
| `npm run lint`    | Lint with ESLint + Prettier                 |
| `npm run format`  | Format with Prettier                        |
| `npm test`        | Run unit tests with Vitest                  |
| `npm run test:watch` | Run tests in watch mode                  |

## Routes

| Route            | Access    | Description                          |
| ---------------- | --------- | ------------------------------------ |
| `/`              | Public    | Landing page                         |
| `/auth/login`    | Public    | Login form                           |
| `/auth/register` | Public    | Registration form                    |
| `/auth/logout`   | Public    | Sign-out action (POST only, no page) |
| `/auth/error`    | Public    | Auth error page                      |
| `/chat`          | Protected | Main chat interface                  |

Protected routes redirect to `/auth/login` if no session is present. The guard is in `src/hooks.server.ts`.

## Auth Pages Layout

All pages share a dark copper aesthetic along with smooth GSAP animations.

## Notes

- After adding new route files, run `npx svelte-kit sync` to regenerate types.
- The dev server must be running alongside the Flask backend (`http://127.0.0.1:5000`) for chat to work.
