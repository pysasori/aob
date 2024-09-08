import time


import pyperclip
import bot.functions as functions
from bot.config import *



def buy_order(start_cord, buy_order, amount_to_buy=1):

    functions.mouse_move_click(start_cord[0] + btn_plus[0], start_cord[1] + btn_plus[1])

    # functions.mouse_move_click(start_cord[0] + input_sell_price[0], start_cord[1] + input_sell_price[1])
    # for i in range(10):
    #     keyboard.press_and_release('backspace')
    # pyperclip.copy(buy_order + 1)
    # keyboard.press_and_release('ctrl + v')
    # time.sleep(0.2)



    functions.mouse_move_click(start_cord[0] + btn_create[0], start_cord[1] + btn_create[1])

    lots_was_bought = functions.search_on_screen(
        'templates_img/yes.bmp',
        0.90,
        [
            start_cord[0],
            start_cord[1],
            len_window[0],
            len_window[1]
        ],
        2
    )
    if lots_was_bought:
        functions.mouse_move_click(lots_was_bought[0], lots_was_bought[1])



def buy_lots(start_cord,  price):
    # amount_to_buy_orders = round((budget - (buy_order * amount_sell)) / buy_order)
    # amount_to_buy_max = round(budget / buy_order / 4)
    amount_to_buy = 1
    #
    # print('amount_to_buy_orders', amount_to_buy_orders)
    # print('amount_to_buy_max', amount_to_buy_max)
    if amount_to_buy > 0:

        functions.mouse_move_click(start_cord[0] + create_orders[0], start_cord[1] + create_orders[1])  # go to orders
        functions.mouse_move_click(start_cord[0] + btn_create_order[0],
                                   start_cord[1] + btn_create_order[1])  # go to menu orders



        buy_order(start_cord, price, amount_to_buy)


