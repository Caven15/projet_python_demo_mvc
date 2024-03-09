from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)

class UserRegisterSchema(UserSchema):
    password = fields.String(required=True, validate=validate.Length(min=6))