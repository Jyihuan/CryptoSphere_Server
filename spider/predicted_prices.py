import numpy as np
from sklearn.linear_model import LinearRegression

def predict_future_prices(data):
    """
    使用线性回归模型预测未来5天的价格

    Parameters:
    data (dict): 包含"last_10_days_prices"和"price"字段的数据字典

    Returns:
    future_prices (list): 预测的未来5天价格列表
    """

    # 提取过去10天的价格数据
    last_10_days_prices = np.array(data["last_10_days_prices"]).reshape(-1, 1)

    # 创建线性回归模型
    model = LinearRegression()

    # 训练模型
    days = np.arange(1, 11).reshape(-1, 1)
    model.fit(days, last_10_days_prices)

    # 预测未来5天的价格
    future_days = np.arange(11, 16).reshape(-1, 1)
    future_prices = model.predict(future_days)

    return future_prices.flatten().tolist()

# 使用示例
# data = {
#     "last_10_days_prices": [
#         70.51, 66.89, 63.31, 62.72, 61.05,
#         63.56, 64.42, 66.60, 66.55, 63.91
#     ],
#     "performance": -9.36,
#     "price": 64.41,
#     "symbol": "ARKB"
# }
#
# future_prices = predict_future_prices(data)
# print("Predicted Future Prices:", future_prices)
