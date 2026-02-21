from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS
from routes.v1.v1 import v1

from db.supabase import supabase

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "http://localhost:5174"])

app.register_blueprint(v1)

if __name__ == '__main__':
    app.run(debug=True)