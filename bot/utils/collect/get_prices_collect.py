import time

import bot.functions as functions
from bot.config import *


def scan_price(start_cord: tuple):

    wait_silver_coin = functions.search_on_screen(
        'templates_img/silver_coin.bmp',
        0.97,
        [
            start_cord[0],
            start_cord[1],
            len_window[0],
            len_window[1]
        ],
        3
    )
    time.sleep(0.13)

    sell_order = functions.scan_prices([
        start_cord[0] + sell_orders[0],
        start_cord[1] + sell_orders[1],
        75,
        20
    ])
    buy_order = functions.scan_prices([
        start_cord[0] + buy_orders[0],
        start_cord[1] + buy_orders[1],
        75,
        20
    ])

    return int(sell_order.replace(",", "")), int(buy_order.replace(",", ""))


def get_prices_collect(start_cord: tuple, dop_cords: list = None):

    functions.mouse_move_click(start_cord[0] + create_orders[0], start_cord[1] + create_orders[1])  # go to orders
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

    sell_order, buy_order = scan_price(start_cord)
    functions.mouse_move_click(start_cord[0] + exit_from_orders[0], start_cord[1] + exit_from_orders[1])
    return sell_order, buy_order


