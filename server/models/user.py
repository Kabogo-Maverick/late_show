# server/models/user.py

from server.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)  # Allow longer hash strings

    def set_password(self, password):
        """Hashes and stores the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks a password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, plain_text_password):
        self.set_password(plain_text_password)

    def __repr__(self):
        return f"<User {self.username}>"
