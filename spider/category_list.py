import yfinance as yf

# List of stock symbols

# stocks = ['ARKB', 'BITB', 'IBIT', 'EZBC', 'FBTC', 'GBTC', 'DEFI', 'BTCO', 'HODL', 'BRRR', 'BTCW']
stocks = ['ARKB', 'IBIT', 'FBTC', 'BTCO', 'HODL', 'BRRR', 'BTCW']


def get_stock_info(symbol, period='10d'):
    try:

        # Fetch historical data for the specified symbol

        stock_info = yf.Ticker(symbol)

        historical_data = stock_info.history(period=period)

        # Get the last 10 days of close prices

        last_10_days_prices = historical_data['Close'][-10:].tolist()

        # Calculate the performance as the percentage change from the oldest to the newest price

        performance = (historical_data['Close'].iloc[-1] - historical_data['Close'].iloc[0]) / \
                      historical_data['Close'].iloc[0] * 100

        # Get the current ask price

        current_price = stock_info.info['ask']

        return current_price, last_10_days_prices, performance

    except Exception as e:

        print(f"Error for {symbol}: {e}")

        return None, None, None


def start():
    result = []
    for stock_symbol in stocks:
        current_price, last_10_days_prices, performance = get_stock_info(stock_symbol)
        if current_price is not None:
            # Append symbol, current price, last 10 days prices, and performance to the lists
            item = {"symbol": stock_symbol, "price": current_price, "last_10_days_prices": last_10_days_prices,
                    "performance": performance}
            result.append(item)
    return result
