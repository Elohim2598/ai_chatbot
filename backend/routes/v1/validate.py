from .v1 import v1

"""
This is the validation route of the client authentication. It returns either 200 or 401.

The workflow for this is the following:

1. Get the token from the request.
2. Validate the token.
3. If the token is valid, return 200.
4. If the token is invalid, return 401.
"""

@v1.route('/validate')
def validate():
    return 'OK'