import time

import bot.functions as functions
from bot.config import *
from .get_prices import scan_price
from .buy_lots import buy_order as buy
from .sell_lots import sell_order as sell


def sell_and_buy_together(start_cord, item):
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

    functions.mouse_move_click(start_cord[0] + my_sell[0], start_cord[1] + my_sell[1])

    while True:
        
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

        btn_sell = functions.search_on_screen(
            'templates_img/btn_sell.bmp',
            0.92,
            [
                start_cord[0],
                start_cord[1],
                len_window[0],
                len_window[1]
            ],
            0.7
        )
        if btn_sell:
            functions.mouse_move_click(btn_sell[0], btn_sell[1])
            try:
                sell_order, buy_order = scan_price(start_cord)
                profit = sell_order - buy_order
                profit_percentage = (profit / sell_order)
                if profit_percentage > 0.165:
                    functions.mouse_move_click(start_cord[0] + 265, start_cord[1] + 423)
                    buy(start_cord,buy_order)
                    time.sleep(0.2)
                    functions.mouse_move_click(btn_sell[0], btn_sell[1])
                sell(start_cord, sell_order)
            except:
                sell(start_cord)
                
            time.sleep(0.15)




        else:
            break