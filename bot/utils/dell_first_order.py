import time

from bot.functions.mouse_control import *
from bot.config import *
import bot.functions as functions



def dell_first_buy_order(start_cord):
    mouse_move_click(start_cord[0] + 1033, start_cord[1] + 468)
    mouse_long_click()
    mouse_move_click(start_cord[0] + 956, start_cord[1] + 307)
    time.sleep(0.2)
    mouse_move_click(start_cord[0] + 956, start_cord[1] + 307)
    time.sleep(0.2)
    mouse_move_click(start_cord[0] + 956, start_cord[1] + 307)
    time.sleep(0.2)


def dell_first_sell_order(start_cord):
    mouse_move_click(start_cord[0] + 1033, start_cord[1] + 468)
    mouse_long_click()
    mouse_move_click(start_cord[0] + 956, start_cord[1] + 581)