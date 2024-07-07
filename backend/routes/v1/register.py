from .v1 import v1

"""
This is the register route. It will register the user in the database.

The workflow for this is the following:

1. Get the username from the request.
2. Get the password from the request.
3. Check if the user exists in the database.
4. If the user does not exist, insert the user into the database.

5. Return a success message.
"""

@v1.route('/validate')
def validate():
    return 'OK'