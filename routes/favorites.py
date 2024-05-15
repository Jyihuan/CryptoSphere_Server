from flask import Blueprint, jsonify, request
from utils import token_required
from services.favorites import create_favorite, get_all_favorites_by_user_id, delete_favorite

favorites_bp = Blueprint('favorites', __name__)


@favorites_bp.route('/create', methods=['POST'])
@token_required
def create():
    symbol = request.json.get('symbol'),
    user_id = request.current_user['user_id']
    result, message = create_favorite(symbol,user_id)
    if result == True:
        return jsonify({'message': message})
    return jsonify({'message': message}), 400


@favorites_bp.route('/delete', methods=['POST'])
def delete():
    symbol = request.json.get('symbol'),
    user_id = request.current_user['user_id']
    deleted = delete_favorite(symbol, user_id)
    if deleted:
        return jsonify({'message': 'Favorite deleted successfully.'})
    else:
        return jsonify({'message': 'Failed to delete favorite.'}), 400


@favorites_bp.route('/update', methods=['POST'])
def update():
    # to do
    return jsonify({'message': 'update Successful!'})


@favorites_bp.route('/retrieve', methods=['GET'])
@token_required
def retrieve():
    user_id = request.current_user['user_id']
    results = get_all_favorites_by_user_id(user_id)
    serialized_results = [result.to_dict() for result in results]
    return jsonify({'message': 'retrieve Successful!', "data": serialized_results})
