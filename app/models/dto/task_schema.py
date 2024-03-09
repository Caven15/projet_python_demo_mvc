from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    description = fields.String(required=True, validate=validate.Length(min=1, max=200))
    user_id = fields.Integer(required=True, validate=validate.Range(min=1))


