from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.extensions import db

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    required = ('guest_id', 'episode_id', 'rating')
    if not all(k in data for k in required):
        abort(400, description="guest_id, episode_id, rating required")

    rating = data['rating']
    if not (1 <= rating <= 5):
        abort(400, description="Rating must be between 1 and 5")

    ap = Appearance(guest_id=data['guest_id'],
                    episode_id=data['episode_id'],
                    rating=rating)
    db.session.add(ap)
    db.session.commit()
    return jsonify(ap.to_dict()), 201
