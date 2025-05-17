"""
Conversation management service.
"""

from src.extensions import db, cache
from src.models.conversation import Conversation
from src.models.message import Message

class ConversationService:
    @staticmethod
    @cache.memoize(60)
    def get_conversation(conversation_id):
        """Get conversation by ID."""
        return Conversation.query.get(conversation_id)
    
    @staticmethod
    @cache.memoize(60)
    def get_user_conversations(user_id):
        """Get all conversations for a user."""
        return Conversation.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def create_conversation(user_id, title=None):
        """Create a new conversation."""
        conversation = Conversation(
            user_id=user_id,
            title=title or "New Conversation"
        )
        db.session.add(conversation)
        db.session.commit()
        return conversation
    
    @staticmethod
    def add_message(conversation_id, content, role):
        """Add a message to a conversation."""
        message = Message(
            conversation_id=conversation_id,
            content=content,
            role=role
        )
        db.session.add(message)
        db.session.commit()
        return message
    
    @staticmethod
    def get_conversation_messages(conversation_id):
        """Get all messages in a conversation."""
        return Message.query.filter_by(conversation_id=conversation_id).order_by(Message.created_at).all()
    
    @staticmethod
    def update_conversation(conversation_id, **kwargs):
        """Update conversation information."""
        conversation = Conversation.query.get(conversation_id)
        if conversation:
            for key, value in kwargs.items():
                if hasattr(conversation, key):
                    setattr(conversation, key, value)
            db.session.commit()
        return conversation
    
    @staticmethod
    def delete_conversation(conversation_id):
        """Delete a conversation and all its messages."""
        conversation = Conversation.query.get(conversation_id)
        if conversation:
            db.session.delete(conversation)
            db.session.commit()
            return True
        return False 