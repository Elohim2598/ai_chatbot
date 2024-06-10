# AI Chatbot

Welcome to the AI Chatbot project! This project aims to build a bot that can understand and respond to user inputs in a conversational manner.

## Installation

To get started with the AI Chatbot, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/elohim2598/ai-chatbot.git
    cd ai-chatbot
    ```

2. **Set up a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install flask
    ```

4. **Run the application**:
    ```sh
    python server.py
    ```

## Contributing

To contribute to this project, follow these steps:

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature/your-feature`).
3. **Commit your changes** (`git commit -m 'Add your feature'`).
4. **Push to the branch** (`git push origin feature/your-feature`).
5. **Open a Pull Request**.

Please ensure your code adheres to the project's coding standards.

## Project Structure

Regarding the folder structure, we plan to organize it as follows:

ai-chatbot/\
├── backend\
│ ├── app.py # Main Flask application\
│ ├── requirements.txt # Python dependencies\
│ ├── Dockerfile # Dockerfile for the backend\
│ ├── .env # Environment variables\
│ ├── models/ # Directory for AI models\
│ │ └── model.py # Code to load/use the Hugging Face model\
│ ├── routes/ # Flask routes\
│ │ ├── init.py\
│ │ └── chatbot.py # Route for chatbot API\
│ ├── static/ # Static files (if any)\
│ └── templates/ # HTML templates (if any)\
│ └── index.html\
├── frontend/\
│ ├── public/\
│ │ └── index.html # Entry point for the Svelte app\
│ ├── src/\
│ │ ├── App.svelte # Main Svelte component\
│ │ ├── components/ # Svelte components\
│ │ │ └── ChatBox.svelte\
│ │ ├── stores/ # Svelte stores\
│ │ │ └── chatbotStore.js\
│ │ └── main.js # Main JavaScript file\
│ ├── package.json # Node.js dependencies\
│ ├── package-lock.json # Lock file for dependencies\
│ ├── rollup.config.js # Rollup configuration for building the Svelte app\
│ └── Dockerfile # Dockerfile for the frontend\
├── tests/\
│ ├── backend/\
│ │ ├── test_app.py # Tests for the Flask app\
│ │ └── test_chatbot.py # Tests for the chatbot API\
│ └── frontend/\
│ └── test_chatbox.js # Tests for the Svelte components\
├── .gitignore # Git ignore file\
├── docker-compose.yml # Docker Compose file for multi-container setup\
├── README.md # Project documentation\
└── LICENSE # License file\

## Backend (Flask)

- **app.py**: Main entry point for the Flask application.
- **requirements.txt**: Lists all the Python dependencies.
- **Dockerfile**: Defines the Docker image for the backend.
- **.env**: Contains environment variables (e.g., API keys, database URLs).
- **models/**: Directory for AI models, with a script to load the Hugging Face model.
- **routes/**: Contains the Flask routes, with a specific route for the chatbot API.
- **static/**: (Optional) Contains static files if needed.
- **templates/**: (Optional) Contains HTML templates if needed.

## Frontend (Svelte)

- **public/**: Contains the main HTML entry point for the Svelte app.
- **src/**: Contains the main Svelte components, stores, and JavaScript files.
  - **App.svelte**: Main Svelte component.
  - **components/**: Directory for additional Svelte components.
  - **stores/**: Directory for Svelte stores.
  - **main.js**: Main JavaScript file to bootstrap the Svelte app.
- **package.json**: Lists Node.js dependencies.
- **package-lock.json**: Lock file for Node.js dependencies.
- **rollup.config.js**: Configuration for Rollup, used to build the Svelte app.
- **Dockerfile**: Defines the Docker image for the frontend.

## Tests

- **tests/backend/**: Contains tests for the Flask backend.
  - **test_app.py**: Tests for the main Flask application.
  - **test_chatbot.py**: Tests for the chatbot API.
- **tests/frontend/**: Contains tests for the Svelte frontend.
  - **test_chatbox.js**: Tests for the Svelte components.

## Root Directory

- **.gitignore**: Specifies files and directories to be ignored by Git.
- **docker-compose.yml**: Defines multi-container Docker applications.
- **README.md**: Project documentation.
- **LICENSE**: License file for the project.

## _Remember we are open to changes so this might not be the final file structure, suggestions are very welcome._


