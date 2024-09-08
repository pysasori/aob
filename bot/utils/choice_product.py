import time
import keyboard
import pyperclip
from bot.functions.mouse_control import *
from bot.config import *


def choice_product(object, back_row):

    #Name

    mouse_move_click(back_row[0] , back_row[1])
    mouse_long_click()
    time.sleep(0.2)
    mouse_move_click(back_row[0]-80, back_row[1])
    pyperclip.copy(object["object"])
    time.sleep(0.2)
    keyboard.press_and_release('ctrl + v')


    #Category if need + add in config rows
    # mouse_move_click(back_row[0] + 80, back_row[1] + 11)
    # time.sleep(0.3)
    # mouse_move_from_point(y=25 * (category[object["category"]] + 1))
    # time.sleep(0.2)
    # mouse_move_from_point(x=150)
    # time.sleep(0.2)
    # mouse_move_from_point(y=25 * (sub_category[object['category']][object["sub_category"]] - 1))
    # mouse_click()
    # time.sleep(0.1)

    #Tier
    mouse_move_click(back_row[0] + 230, back_row[1] + 11)
    mouse_move_from_point(y=25 * (tier[object["tier"]] + 1))
    mouse_click()

    # Enchantment
    mouse_move_click(back_row[0] + 380, back_row[1] + 11)
    mouse_move_from_point(y=25 * (enchantment[object["enchantment"]] + 1))
    mouse_click()
