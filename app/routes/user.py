from flask_jwt_extended import jwt_required
from app import app
from app.controllers.User_controller import User_controller

@app.route('/users', methods=['GET'])
def get_users():
    return User_controller.get_all()

@app.route('/user/update/<int:id>', methods=['POST'])
@jwt_required()
def update_user(id):
    return User_controller.update(id)

@app.route('/user/delete/<int:id>', methods=['POST'])
@jwt_required()
def delete_user(id):
    return User_controller.delete(id)