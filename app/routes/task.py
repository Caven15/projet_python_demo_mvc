from app import app
from app.controllers.Task_controller import Task_controller

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return Task_controller.get_all()

@app.route('/task/create', methods=['POST'])
def create_task():
    return Task_controller.create()

@app.route('/task/update/<int:id>', methods=['POST'])
def update_task(id):
    return Task_controller.update(id)

@app.route('/task/delete/<int:id>', methods=['POST'])
def delete_task(id):
    return Task_controller.delete(id)

