# user.py
from . import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        # 将用户模型转换为字典格式
        return {
            'username': self.username,
            "email": self.email
            # 其他属性...
        }
