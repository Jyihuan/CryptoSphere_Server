from . import db


class FavoritesModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_model.id'), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)

    # 添加一个关系字段，以便于在查询时能够方便地访问用户对象
    user = db.relationship('UserModel', backref=db.backref('selections', lazy=True))

    def to_dict(self):
        # 将用户模型转换为字典格式
        return {
            'symbol': self.symbol,
        }

    def __repr__(self):
        return f"<FavoritesModel user_id={self.user_id}, currency_code={self.symbol}>"
