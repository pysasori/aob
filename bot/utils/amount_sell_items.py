import time


import pyperclip
from bot.functions.mouse_control import *
from bot.config import *
import bot.functions as functions



def amount_sell_items(start_cord):
    mouse_move_click(start_cord[0] + 1033, start_cord[1] + 468)
    mouse_long_click()
    time.sleep(0.3)

    order_cords = [start_cord[0] + 285, start_cord[1] + 575]


    number_orders = 0
    summ_orders = 0

    # for firsts 3 orders
    for i in range(3):
        try:
            number_orders = int ( functions.scan_prices([order_cords[0], order_cords[1], 40, 15]))
            print('number_orders',number_orders)
            summ_orders += int(functions.scan_prices([order_cords[0]+250, order_cords[1], 25, 15]))
            print('summ_orders', summ_orders)
            order_cords[1] += 50
        except:
            continue

    functions.mouse_move(order_cords[0],order_cords[1]-30)
    while True:
        try:

            new_number_orders = int(functions.scan_prices([order_cords[0], order_cords[1], 25, 15]))
            if new_number_orders > number_orders:
                summ_orders += int(functions.scan_prices([order_cords[0] + 250, order_cords[1], 25, 15]))
                print('new_number_orders', new_number_orders)
                functions.mouse_scroll(51)
                number_orders = new_number_orders


            else:
                new_number_orders = int(functions.scan_prices([order_cords[0]+250, order_cords[1], 25, 15]))
                break
        except:
            break
    print('result', summ_orders)
    return summ_orders

