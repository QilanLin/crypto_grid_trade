# price_checker.py
import ccxt
import config

exchange = ccxt.binance()

def get_current_price():
    try:
        ticker = exchange.fetch_ticker(config.SYMBOL)
        return ticker['last']
    except Exception as e:
        print(f"获取价格时出错: {e}")
        return None

def is_price_in_range(price):
    for lower, upper in config.PRICE_RANGES:
        if lower < price < upper:
            return lower, upper
    return None
