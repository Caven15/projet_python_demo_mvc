from flask import jsonify, request
from marshmallow import ValidationError
from app.models.db.db_model import Task
from app.models.dto.task_schema import TaskSchema
from app.services.session_scope import session_scope
from flask_restful import Resource

class Task_controller(Resource):
    def get_all():
        with session_scope() as session:
            tasks = session.query(Task).all()
            task_schema = TaskSchema(many=True)
            serialized_tasks = task_schema.dump(tasks)
        return jsonify(serialized_tasks), 200

    def create():
        task_schema = TaskSchema()
        errors = task_schema.validate(request.json)
        if errors:
            return jsonify(errors), 400
        new_task_data = task_schema.load(request.json)
        new_task = Task(**new_task_data)
        with session_scope() as session:
            session.add(new_task)
        serialized_new_task = task_schema.dump(new_task)
        return jsonify(serialized_new_task), 201

    def update(id):
        task_schema = TaskSchema()
        try:
            data = task_schema.load(request.json, partial=True)
        except ValidationError as e:
            return jsonify(e.messages), 400

        with session_scope() as session:
            task = session.query(Task).filter_by(id=id).first()
            if task:
                for key, value in data.items():
                    setattr(task, key, value)
                serialized_task = task_schema.dump(task)
                return jsonify(serialized_task), 200
            else:
                return {'message': 'Aucune tâche trouvée'}, 404


    def delete(id):
        with session_scope() as session:
            task = session.query(Task).filter_by(id=id).first()
            if task:
                session.delete(task)
                return '', 204
            else:
                return {'message': 'Aucune tâche trouvée'}, 404
