"""
Message model for storing conversation messages.
"""

from datetime import datetime
from src.extensions import db

class Message(db.Model):
    """Message model for chat interactions."""
    
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'user' or 'assistant'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Message {self.id}>'
    
    def to_dict(self):
        """Convert message object to dictionary."""
        return {
            'id': self.id,
            'conversation_id': self.conversation_id,
            'content': self.content,
            'role': self.role,
            'created_at': self.created_at.isoformat()
        } 