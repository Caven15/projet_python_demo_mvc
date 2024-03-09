from app import app
from app.controllers.Auth_controller import Auth_controller

@app.route('/auth/login', methods=['POST'])
def login():
    return Auth_controller.login()


@app.route('/auth/register', methods=['POST'])
def register():
    return Auth_controller.register()
