from .v1 import v1

@v1.route('/hello')
def hello():
    return 'Welcome to our chatbot demonstration!'