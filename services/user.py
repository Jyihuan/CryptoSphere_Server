from models.user import UserModel


def get_all_users():
    return UserModel.query.all()


def get_user_by_username(username):
    return UserModel.query.filter_by(username=username).first()


def get_user_by_id(user_id):
    return UserModel.query.filter_by(id=user_id).first()
