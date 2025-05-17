"""
User management service.
"""

from src.extensions import db, cache
from src.models.user import User

class UserService:
    @staticmethod
    @cache.memoize(300)
    def get_user_by_id(user_id):
        """Get user by ID."""
        return User.query.get(user_id)
    
    @staticmethod
    @cache.memoize(300)
    def get_user_by_username(username):
        """Get user by username."""
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def create_user(username, email, password_hash):
        """Create a new user."""
        user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def update_user(user_id, **kwargs):
        """Update user information."""
        user = User.query.get(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user_id):
        """Delete a user."""
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False 