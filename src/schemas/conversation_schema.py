"""
Conversation and message validation schemas.
"""

from marshmallow import Schema, fields, validate

class MessageSchema(Schema):
    """Schema for message data validation."""
    
    id = fields.Int(dump_only=True)
    conversation_id = fields.Int(required=True)
    content = fields.Str(required=True, validate=validate.Length(min=1))
    role = fields.Str(required=True, validate=validate.OneOf(['user', 'assistant']))
    created_at = fields.DateTime(dump_only=True)

class ConversationSchema(Schema):
    """Schema for conversation data validation."""
    
    id = fields.Int(dump_only=True)
    title = fields.Str(validate=validate.Length(max=200))
    user_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_active = fields.Boolean(dump_only=True)
    messages = fields.Nested(MessageSchema, many=True, dump_only=True)

class ConversationUpdateSchema(Schema):
    """Schema for conversation update validation."""
    
    title = fields.Str(validate=validate.Length(max=200))
    is_active = fields.Boolean() 