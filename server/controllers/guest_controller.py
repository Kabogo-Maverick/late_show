from flask import Blueprint, request, jsonify, abort
from server.models.guest import Guest
from server.extensions import db

guest_bp = Blueprint("guests", __name__)

@guest_bp.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200

@guest_bp.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    if not data.get('name') or not data.get('occupation'):
        abort(400, description="Name and occupation required")
    guest = Guest(name=data['name'], occupation=data['occupation'])
    db.session.add(guest)
    db.session.commit()
    return jsonify(guest.to_dict()), 201

@guest_bp.route('/guests/<int:id>', methods=['GET'])
def show_guest(id):
    guest = Guest.query.get_or_404(id)
    return jsonify(guest.to_dict()), 200

@guest_bp.route('/guests/<int:id>', methods=['PATCH'])
def update_guest(id):
    guest = Guest.query.get_or_404(id)
    data = request.get_json()
    if 'name' in data: guest.name = data['name']
    if 'occupation' in data: guest.occupation = data['occupation']
    db.session.commit()
    return jsonify(guest.to_dict()), 200

@guest_bp.route('/guests/<int:id>', methods=['DELETE'])
def delete_guest(id):
    guest = Guest.query.get_or_404(id)
    db.session.delete(guest)
    db.session.commit()
    return "", 204
