import time


from bot.functions.mouse_control import *
from bot.config import *
import bot.functions as functions


def check_datas(start_cord):
    lust_time = 0

    # for i in range(4):

    #days = functions.scan_prices([first_order_cords[0], first_order_cords[1], 23, 50])
    buy_hours = functions.scan_prices([start_cord[0] + 612, start_cord[1] + 279, 50, 50])
    sell_hours = functions.scan_prices([start_cord[0] + 612, start_cord[1] + 569, 50, 50])
    try:
        buy_lust_time = buy_hours
        sell_lust_time = sell_hours
        print('buy_lust_time', buy_lust_time)
        print('sell_lust_time', sell_lust_time)
    except:
        return Exception

    return buy_lust_time, sell_lust_time




def check_orders_lust_time(start_cord):
    """
    Проверка даты ордера продажи
    """

    mouse_move_click(start_cord[0] + 1033, start_cord[1] + 468)
    mouse_long_click()
    time.sleep(0.3)
    return check_datas(start_cord)









