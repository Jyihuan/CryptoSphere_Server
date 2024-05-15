from flask import Blueprint, jsonify, request
from spider.category_list import start
from spider.predicted_prices import predict_future_prices

crypto_bp = Blueprint('crypto', __name__)


@crypto_bp.route('/list', methods=['GET'])
def list():
    df = start()
    return jsonify({'message': 'Query Successful!', 'data': df})


@crypto_bp.route('/predicted', methods=['POST'])
def predicted():
    result = predict_future_prices(request.json)
    print("调用预测接口",result)
    return jsonify({'message': 'predicted Successful!', 'data': result})
