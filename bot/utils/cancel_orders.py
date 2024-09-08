import bot.functions as functions
from bot.config import *


def cancel_orders(start_cord):
    functions.mouse_move_click(start_cord[0] + my_orders[0], start_cord[1] + my_orders[1])
    for i in range(3):
        functions.mouse_move_click(start_cord[0] + cancel_buy_order[0], start_cord[1] + cancel_buy_order[1], t=0.1)
        functions.mouse_move_click(start_cord[0] + cancel_sell_order[0], start_cord[1] + cancel_sell_order[1], t=0.1)
