from flask import Blueprint

auth = Blueprint("auth",__name__)

@auth.post('/register')
def register():
    return "User registered"

@auth.route('/me')
def me():
    return {"User registered":"user"}