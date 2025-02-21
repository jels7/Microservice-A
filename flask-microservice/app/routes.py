from flask import Blueprint, jsonify, request

bp = Blueprint('api', __name__)

@bp.route('/api/resource', methods=['GET'])
def get_resource():
    return jsonify({"message": "Resource retrieved successfully"}), 200

@bp.route('/api/resource', methods=['POST'])
def create_resource():
    data = request.get_json()
    return jsonify({"message": "Resource created successfully"}), 201

@bp.route('/api/resource/<int:id>', methods=['PUT'])
def update_resource(id):
    data = request.get_json()
    return jsonify({"message": "Resource updated successfully"}), 200

@bp.route('/api/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    return jsonify({"message": "Resource deleted successfully"}), 204