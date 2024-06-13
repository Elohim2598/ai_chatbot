from .v1 import v1

@v1.route('/heartbeat')
def heartbeat():
    return 'OK'