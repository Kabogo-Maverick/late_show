from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.models.user import User
from server.extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return {"error": "Username and password required"}, 400

    if User.query.filter_by(username=data['username']).first():
        return {"error": "Username already exists"}, 409

    user = User(username=data['username'])
    user.password = data['password']
    db.session.add(user)
    db.session.commit()
    return {"message": "User created"}, 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or not user.check_password(data.get('password', '')):
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(identity=user.id)
    return {"token": token}, 200
