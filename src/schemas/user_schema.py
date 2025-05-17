"""
User validation schemas.
"""

from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    """Schema for user data validation."""
    
    id = fields.Int(dump_only=True)
    username = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=80)
    )
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(min=8)
    )
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_active = fields.Boolean(dump_only=True)

class UserUpdateSchema(Schema):
    """Schema for user update validation."""
    
    username = fields.Str(
        validate=validate.Length(min=3, max=80)
    )
    email = fields.Email()
    password = fields.Str(
        load_only=True,
        validate=validate.Length(min=8)
    ) 