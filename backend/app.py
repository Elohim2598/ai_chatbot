from flask import Flask
from routes.v1.v1 import v1

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.register_blueprint(v1)

if __name__ == '__main__':
    app.run(debug=True)