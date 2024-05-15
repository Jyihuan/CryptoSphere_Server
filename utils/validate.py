from functools import wraps
from flask import request, jsonify
from utils.jwt_utils import decode_token


def token_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # 获取请求中的 token
        token = request.headers.get('Authorization')

        # 如果 token 不存在，则返回错误信息
        if not token:
            return jsonify({'message': 'Token is missing.'}), 401

        # 解密和验证 token
        result = decode_token(token)

        if 'error' in result:
            return jsonify(result), 401
        else:
            # 将解密后的 token payload 存储在 request 对象中，以便后续路由函数使用
            request.current_user = result
            return func(*args, **kwargs)

    return decorated_function
