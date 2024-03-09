from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError
from app.models.db.db_model import User
from app.models.dto.User_schema import UserSchema

from app.services.session_scope import session_scope

class User_controller(Resource):
    def get_all():
        with session_scope() as session:
            users = session.query(User).all()
            user_schema = UserSchema(many=True)
            serialized_users = user_schema.dump(users)
        return jsonify(serialized_users), 200

    def update(id):
        user_schema = UserSchema()
        try:
            data = user_schema.load(request.json, partial=True)
        except ValidationError as e:
            return jsonify(e.messages), 400

        with session_scope() as session:
            user = session.query(User).filter_by(id=id).first()
            if user:
                for key, value in data.items():
                    setattr(user, key, value)
                serialized_user = user_schema.dump(user)
                return jsonify(serialized_user), 200
            else:
                return {'message': 'Aucun utilisateur trouvé'}, 404

    def delete(id):
        with session_scope() as session:
            user = session.query(User).filter_by(id=id).first()
            if user:
                session.delete(user)
                return '', 204
            else:
                return {'message': 'Aucun utilisateur trouvé'}, 404