import time

import bot.functions as functions
from bot.config import *


def lots_was_bought(start_cord: tuple):
    lots_was_bought = functions.checking_object_on_screen(
        'templates_img/lots_was_bought.bmp',
        0.90,
        [
            start_cord[0],
            start_cord[1],
            len_window[0],
            len_window[1]
        ]
    )
    if lots_was_bought:
        functions.mouse_move_click(lots_was_bought[0], lots_was_bought[1])

        time.sleep(1.5)
        take_all = functions.search_on_screen(
            'templates_img/take_all.bmp',
            0.85,
            [
                start_cord[0],
                start_cord[1],
                len_window[0],
                len_window[1]
            ]
        )

        functions.mouse_move_click(start_cord[0] + take_all[0], start_cord[1] + take_all[1])

    time.sleep(1)
