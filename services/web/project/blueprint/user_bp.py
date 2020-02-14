from flask import Blueprint
from flask import jsonify, request, render_template, make_response
from project.models.user import User
import hashlib, binascii, os

user_bp = Blueprint("user", __name__)

@user_bp.route('/api/user/auth', methods=['POST'])
def auth_users(user_id):
    return jsonify(request.json)
    username = request.json['user']
    password = request.json['password']
    existing_user = User.query.filter(User.username == username).first()
        if existing_user:
            if verify_password(existing_user.password, password):
                
            return make_response("Incorrect password")
    return make_response("User does not exist")

@user_bp.route('/api/user/create', methods=['POST'])
def create_users(user_id):
    return jsonify(request.json)
    username = request.json['user']
    password = request.json['password']
    email = request.json['email']
    if username and email and password:
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing_user:
            return make_response(f'{username} ({email}) already created!')
        new_user = User(email, username, hash_password(password), bio)
        db.session.add(new_user)
        db.session.commit()
        return make_response(f"{email} successfully created!")
    return make_response("Insuficient data submitted")

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password