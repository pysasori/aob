import time


import pyperclip
from bot.functions.mouse_control import *
from bot.config import *
import bot.functions as functions


#
# def check_datas(start_cord):
#     summ = 0
#     first_order_cords = [start_cord[0] + 528, start_cord[1] + 279]
#     for i in range(4):
#         amount = functions.scan_prices([first_order_cords[0], first_order_cords[1], 50, 50])
#         try:
#             summ += int(amount)
#         except:
#             print('pass')
#         first_order_cords[1] = first_order_cords[1] + 50
#     return summ


def amount_buy_items(start_cord):
    """
    check amount items in buy  orders
    """

    # mouse_move_click(start_cord[0] + 1033, start_cord[1] + 468)
    # mouse_long_click()

    cords = [start_cord[0] + 700, start_cord[1] + 433, 350, 50]
    for i in range(4):

        find = functions.search_on_screen('templates_img/edit.bmp', cords=cords, search_time=0.2)
        if find:
            return 4 - i
        cords[1] -= 50

    return 0


def amount_sell_items(start_cord):
    """
    check amount items in sell  orders
    """

    # mouse_move_click(start_cord[0] + 1033, start_cord[1] + 468)
    # mouse_long_click()

    cords = [start_cord[0] + 700, start_cord[1] + 714, 350, 50]
    for i in range(4):

        find = functions.search_on_screen('templates_img/edit.bmp', cords=cords, search_time=0.2)
        if find:
            return 4 - i
        cords[1] -= 50
    return 0