from flask import Blueprint, jsonify, request
from services.user import get_user_by_username, get_user_by_id
from utils import token_required
from utils.jwt_utils import generate_token, decode_token

user_bp = Blueprint('user', __name__)

# 用于生成 token 的密钥，可以是随机字符串
SECRET_KEY = 'your_secret_key'


@user_bp.route('/login', methods=['POST'])
def login():
    # 获取请求中的 JSON 数据
    request_data = request.json

    # 从 JSON 数据中提取用户名和密码
    username = request_data.get('username')
    password = request_data.get('password')

    # 获取用户对象
    user = get_user_by_username(username)
    if user is None:
        return jsonify({'error': 'User not found.'}), 404
        # 比较用户提供的加密后密码与数据库中存储的密码是否一致
    if password == user.password:
        # 生成 token
        token = generate_token(user.id)
        return jsonify({'message': 'Login Successful!', 'data': token})
    else:
        return jsonify({'error': 'Incorrect password.'}), 401


@user_bp.route('/info', methods=['GET'])
@token_required
def info():
    # to do
    user_object = request.current_user
    result = get_user_by_id(user_object['user_id'])
    return jsonify({'message': 'get user info Successful!','data':result.to_dict()})

@user_bp.route('/register', methods=['POST'])
def register():
    # to do
    return jsonify({'message': 'register Successful!'})
