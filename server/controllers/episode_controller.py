from flask import Blueprint, jsonify, abort
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.extensions import db

episode_bp = Blueprint("episodes", __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    eps = Episode.query.all()
    return jsonify([e.to_dict() for e in eps]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def show_episode(id):
    ep = Episode.query.get_or_404(id)
    return jsonify(ep.to_dict(include_relationships=True)), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get_or_404(id)
    db.session.delete(ep)
    db.session.commit()
    return "", 204
