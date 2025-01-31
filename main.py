# main.py
import time
from price_checker import get_current_price, is_price_in_range
from email_alert import send_email
import config

if __name__ == "__main__":
    while True:
        price = get_current_price()
        if price is not None:
            print(f"{config.SYMBOL} 最新价格: {price}")
            range_tuple = is_price_in_range(price)
            if range_tuple:
                lower, upper = range_tuple
                subject = f"{config.SYMBOL} 价格预警"
                message = f"{config.SYMBOL} 当前价格为 {price}，已进入预设的价格区间 ({lower}, {upper})。"
                # send_email(subject, message)
                print(subject, message)
        time.sleep(10)  # 每10秒检查一次价格
