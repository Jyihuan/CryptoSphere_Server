import jwt
import datetime
from jwt.exceptions import ExpiredSignatureError

# 用于生成 token 的密钥，可以是随机字符串
SECRET_KEY = 'aaa_bbb_ccc'


def generate_token(user_id):
    # 生成 token
    token = jwt.encode({'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)},
                       SECRET_KEY)
    return token


def decode_token(token):
    try:
        # 解密 token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except ExpiredSignatureError:
        # token 已过期
        return {'error': 'Token has expired.'}
    except jwt.InvalidTokenError:
        # token 无效
        return {'error': 'Invalid token.'}
