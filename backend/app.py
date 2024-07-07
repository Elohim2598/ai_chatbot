from flask import Flask
from routes.v1.v1 import v1

from db.supabase import supabase

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'AI Chatbot Demonstration - Svelte + Supabase + Python + Flask'

app.register_blueprint(v1)

if __name__ == '__main__':
    app.run(debug=True)