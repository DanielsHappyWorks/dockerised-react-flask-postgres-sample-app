from project.models.base import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    auth_level = db.Column(db.String(128), default=True, nullable=False)
    bio = db.Column(db.UnicodeText, default=True, nullable=False)

    def __init__(self, email, username, password, bio):
        self.username = username
        self.password = password
        self.email = email
        self.active = False
        self.auth_level = "user"
        self.bio = ""