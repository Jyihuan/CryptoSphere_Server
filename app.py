from flask import Flask
from flask_cors import CORS
from routes.user import user_bp
from routes.favorites import favorites_bp
from routes.crypto import crypto_bp
from config.dbconfig import SQLALCHEMY_DATABASE_URI
from models import db


def create_app():
    app = Flask(__name__)
    # 配置数据库连接参数
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 配置数据库
    db.init_app(app)
    # 创建所有表
    with app.app_context():
        from models.user import UserModel
        from models.favorites import FavoritesModel
        db.create_all()

    # 配置蓝图
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(favorites_bp, url_prefix='/favorites')
    app.register_blueprint(crypto_bp, url_prefix='/crypto')

    # 允许跨域
    CORS()

    @app.route('/')
    def hello_world():  # put application's code here
        return 'hello world1'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
