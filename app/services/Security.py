from datetime import timedelta
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

# Fonction pour hacher et saler le mot de passe
def hash_password(password):
    return generate_password_hash(password)

# Fonction pour vérifier le mot de passe
def verify_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def generate_jwt_token(user, additional_claims=None, expires_in_hours=1):
    token_claims = {
        'username': user.username
    }
    # Ajouter des claims supplémentaires s'ils sont fournis
    if additional_claims:
        token_claims.update(additional_claims)
    # Définir la durée de validité du token en heures
    expires_in = timedelta(hours=expires_in_hours)
    # Créer le token avec les claims et la durée de validité définis
    access_token = create_access_token( identity=str(user.id),
                                        additional_claims=token_claims,
                                        expires_delta=expires_in)
    return access_token

