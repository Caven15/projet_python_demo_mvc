from flask import jsonify, request
from flask_restful import Resource
from app.models.db.db_model import User
from app.models.dto.User_schema import UserRegisterSchema
from app.services.Security import generate_jwt_token, hash_password, verify_password
from app.services.session_scope import session_scope

class Auth_controller(Resource):
    def login():
        user_schema = UserRegisterSchema(only=("email", "password"))
        errors = user_schema.validate(request.json)
        if errors:
            return jsonify(errors), 400
        
        email = request.json['email']
        password = request.json['password']
        
        with session_scope() as session:
            user = session.query(User).filter_by(email=email).first()
            if user and verify_password(user.password, password):
                additional_claims = {'role': 'utilisateur'}
                access_token = generate_jwt_token(user, additional_claims, expires_in_hours=2)
                return jsonify(access_token=access_token), 200
            else:
                return {'message': 'Nom d\'utilisateur ou mot de passe incorrect'}, 401
    
    def register():
        # Valider les données d'entrée avec Marshmallow
        user_schema = UserRegisterSchema()
        errors = user_schema.validate(request.json)
        if errors:
            return jsonify(errors), 400
        
        # Récupérer les données d'entrée
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        
        # Hacher le mot de passe
        hashed_password = hash_password(password)
        
        # Vérifier si l'utilisateur existe déjà
        with session_scope() as session:
            existing_user = session.query(User).filter_by(email=email).first()
            if existing_user:
                return {'message': 'Cet utilisateur existe déjà'}, 400
        
            # Créer un nouvel utilisateur avec le mot de passe haché
            new_user = User(username=username, email=email, password=hashed_password)
            session.add(new_user)
        
        return {'message': 'Utilisateur enregistré avec succès'}, 201


