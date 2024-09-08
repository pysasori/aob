import time

import bot.functions as functions
from bot.config import *


def get_amount_trades(start_cord: tuple, dop_cords: list = None):

    if dop_cords:
        x, y = functions.search_on_screen('templates_img/buy_order.bmp',
                                   cords=dop_cords
                                   )
        functions.mouse_move_click(x, y)

    else:
        functions.mouse_move_click(start_cord[0] + btn_create_order[0],
                                   start_cord[1] + btn_create_order[1])  # go to menu orders

    pull_out_menu = functions.checking_object_on_screen(
        'templates_img/pull_out_menu.bmp',
        0.99,
        [
            start_cord[0],
            start_cord[1],
            len_window[0],
            len_window[1]
        ]
    )
    if pull_out_menu:
        functions.mouse_move_click(pull_out_menu[0], pull_out_menu[1])
    cords = [1050, 465]
    amounts = []
    for i in range(18):
        try:
            functions.mouse_move(start_cord[0] + cords[0], start_cord[1] + cords[1])
            x, y = functions.search_on_screen('templates_img/sold.bmp', threshold=0.75,
                                              cords=[start_cord[0], start_cord[1], len_window[0], len_window[1]])

            time.sleep(0.15)
            amount = functions.scan_prices([x + 28, y-3, 36, 16])
            #time.sleep(2)
            cords[0] -= 12.5
            try:
                amount_int = int(amount.split('\n')[0])
                amounts.append(amount_int)
            except:
                pass
        except:
            break

    print(amounts)
    return amounts