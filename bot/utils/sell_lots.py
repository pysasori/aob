import time

import bot.functions as functions
from bot.config import *


def sell_order(start_cord, sell_order=None):
    functions.mouse_move_click(start_cord[0] + 265, start_cord[1] + 402)

    functions.mouse_move_click(start_cord[0] + btn_minus[0], start_cord[1] + btn_minus[1])

    functions.mouse_move_click(start_cord[0] + btn_create[0], start_cord[1] + btn_create[1])

    time.sleep(0.15)

    ok = functions.checking_object_on_screen(
        'templates_img/ok.bmp',
        0.92,
        [
            start_cord[0],
            start_cord[1],
            len_window[0],
            len_window[1]
        ]
    )
    if ok:
        functions.mouse_move_click(ok[0], ok[1])

    btn_create_exist = functions.checking_object_on_screen(
        'templates_img/create.bmp',
        0.92,
        [
            start_cord[0],
            start_cord[1],
            len_window[0],
            len_window[1]
        ]
    )

    if btn_create_exist:
        functions.mouse_move_click(start_cord[0] + 264, start_cord[1] + 352)
        functions.mouse_move_click(start_cord[0] + btn_create[0], start_cord[1] + btn_create[1])


def sell_lots(start_cord, price) -> int:
    # functions.mouse_move_click(start_cord[0] + my_sell[0], start_cord[1] + my_sell[1])
    amount = 0
    while True:
        btn_sell = functions.search_on_screen(
            'templates_img/btn_sell.bmp',
            0.92,
            [
                start_cord[0],
                start_cord[1],
                len_window[0],
                len_window[1]
            ],
            1
        )
        if btn_sell:
            functions.mouse_move_click(btn_sell[0], btn_sell[1])
            sell_order(start_cord, price)
        else:
            break
    return amount
