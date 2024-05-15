from models.favorites import FavoritesModel
from models import db


def get_all_favorites_by_user_id(user_id):
    return FavoritesModel.query.filter_by(user_id=user_id).all()


def create_favorite(symbol,user_id):
    # 检查是否已经存在相同用户对相同项目的收藏记录
    existing_favorite = FavoritesModel.query.filter_by(user_id=user_id, symbol=symbol).first()
    if existing_favorite:
        return False, "You have already favorited this item."

    try:
        # 创建 FavoritesModel 对象
        favorite = FavoritesModel(
            user_id=user_id,
            symbol=symbol
        )

        # 将对象添加到会话
        db.session.add(favorite)

        # 提交会话以将更改保存到数据库
        db.session.commit()

        return True, "Favorite created successfully"
    except Exception as e:
        # 如果发生错误，回滚会话以撤销更改
        db.session.rollback()
        return False, str(e)


def delete_favorite(symbol, user_id):
    favorite = FavoritesModel.query.filter_by(symbol=symbol, user_id=user_id).first()
    if favorite:
        # Delete the favorite record from the database
        db.session.delete(favorite)
        db.session.commit()
        return True
    else:
        return False
