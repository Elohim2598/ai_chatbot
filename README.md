# AI Chatbot

Welcome to the AI Chatbot project! This project aims to build a bot that can understand and respond to user inputs in a conversational manner.

## Installation

To get started with the AI Chatbot, follow these steps:

**BACKEND:**
1. **Install Python 3**.
2. Once inside the directory **`/<project-name>/backend`**, run the following command: `python -m venv .venv`.
3. This will create the **virtual environment** for your project.
4. Next you're looking to **activate your environment** which is done after running the **`activate`** script. It can be found at `<project-name>/backend/.venv/Scripts`.<br /><br />
5. **Once inside the `Scripts` folder**, you can run `source activate` to activate your environment.<br /><br /> Alternatively, if **you're still at the `<project-name>/backend` directory**, you can **run `source /.venv/Scripts/activate`** and that will achieve the same result.<br /><br />
6. At the **`<project-name>/backend` directory**, you can run `pip install -r requirements.txt` to **install the project dependencies.**
7. Once installed, you can run bash command `flask run` or `flask run --debug` to **start the server.**

**This project depends on `.env` variables. You can contact the project administrator to receive them or create your own.**

<hr />

**FRONTEND:**
1. You basically have to set up **Svelte** with **Vite**.
2. Should be pretty easy since you just have to do **`pnpm i`** or **`npm i`** after opening bash **in the frontend directory.**
3. **Run the project** with `pnpm dev` or `npm run dev`.


## Contributing

To contribute to this project, follow these steps:
1. **Create a new folder with the project identifier.**
2. **Initialize `git` with the bash command `git init`.**
3. **Get the SSH of the source project i.e `git@github.com:Elohim2598/ai_chatbot.git` or from your own fork.**<sub>( it can be found under the code button in SSH tab. )</sub>
4. **Run the bash command `git remote add origin git@github.com:Elohim2598/ai_chatbot.git` <br /> or <br /> `git remote add origin <fork-ssh-goes-here>`.**
5. **Run the bash command `git pull`.**
6. **Checkout to your feature branch with bash command `git checkout -b <feature-name>`.**
7. **Make changes, create new files etc.**
8. **Push changes to repo with `git push -u origin <feature-name>`.**
9. **Create Pull Request through the Pull Request section of the project.**
10. **Request Review.**
11. **PR is merged after passing review.**

Please ensure your code adheres to the project's coding standards.

## Project Structure

Regarding the folder structure, we plan to organize it as follows:

**With respect to backend:**
```txt
backend/
├── .venv # Scripts and dependencies for the backend.
├── db/
│   ├── supabase.py
│   └── --------------------
├── routes/
│   └── v1/
│       ├── handlers/
│       │   ├── heartbeat.py
│       │   ├── hello.py
│       │   ├── <more-handlers>.py
│       │   └── --------------------
│       ├── v1.py # Contains handlers and wraps them with `/api/v1/`.
│       └── --------------------
├── services/
│   ├── chat.py
│   ├── <more-services>.py
│   └── --------------------
├── app.py
├── .env # Contains your environment variables.
├── requirements.txt # Contains project requirements.
└── --------------------
frontend
---------
.gitignore
README.md

```

## Root Directory

- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: Project documentation.
- **LICENSE**: License file for the project.

<hr />

### Project documentation is `in progress`.