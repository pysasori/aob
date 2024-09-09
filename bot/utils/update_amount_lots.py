import time
import keyboard

import functions
from config import NPC_CORDS
from utils import choice_product, get_prices


def update_amount_lots(start_cord, obj_lists):
    number = functions.read_from_file()
    try:

        if number >= len(obj_lists):
            return len(obj_lists)


        keyboard.press_and_release('esc')

        # Activate auction
        functions.mouse_move_click(start_cord[0] + NPC_CORDS[0], start_cord[1] + NPC_CORDS[1])

        coin_cord = functions.search_on_screen('templates_img/silver_amount_coins.bmp')

        money = functions.read_text([coin_cord[0] + 22, coin_cord[1], 85, 22])
        print(money)
        if 'k' in money:
            money = int(money.split('k')[0]) * 1000
        elif 'm' in money:
            money = int(money.split('m')[0]) * 1000 * 1000

        back_row_cords = functions.search_on_screen(
            'templates_img/back_row.bmp',
            0.90,
        )
        money = int(money)

        choice_product(obj_lists[number], back_row_cords)
        time.sleep(0.2)
        print('+')

        ### Получаем цены
        sell_order, buy_order = get_prices(start_cord)

        if sell_order * 10 < money:
            number = number + 1
            functions.write_to_file(number)
        print(number)
        return number
    except:
        return number