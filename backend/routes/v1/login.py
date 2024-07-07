from  .v1 import v1

"""
This is the login route. The login route is supposed to check against the database if the user exists or if the password exists or if it is correct.

The workflow for this is the following:

1. Get the username from the request.
2. Get the password from the request.
3. Check if the user exists in the database.
4. Check if the password exists in the database.
5. Check if the password is correct.

6.1. Generate a 32 bit token for the user.
6.2. Store the token in the database. We'll use the non-standard expiry time of the token which will be 1 hour expiry.
6.3. Encode the token in the JWT Token.

7. If everything is correct, we attach a JWT token to the response
8. The token is set in cookies when it reaches the browser.

Next time the client calls the API's protected route, the token is sent alongside with the request which will be validated by our authentication guard on the route.
"""

@v1.route("/auth/login")
def login():
    return 'OK'
    