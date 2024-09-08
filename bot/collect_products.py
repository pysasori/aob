import time
import utils
import functions
from config import *


# while True:
#     mouse_move(820, 370)
#
#     mouse_click_and_move(820, 295)
#     read_text([369, 297, 200, 75])
#     time.sleep(3)





if __name__ == "__main__":
    while True:
        try:
            start_cord = functions.search_on_screen('templates_img/icon_game.bmp')
            # For activate window
            functions.mouse_move_click(start_cord[0] + default_shift_start[0], start_cord[1] + default_shift_start[1])
            #keyboard.press_and_release('esc')
            # Activate auction
            #functions.mouse_move_click(start_cord[0] + auction_cord[0], start_cord[1] + auction_cord[1])
            old_product_name = ''
            while True:
                try:
                    product_name = functions.read_text([start_cord[0] + 359, start_cord[1] + 288, 444, 75])
                    if old_product_name != product_name:

                        sell_order, buy_order = utils.get_prices_collect(start_cord)

                        if ((1 - buy_order / sell_order) > 0.15) :
                            amount_trades = utils.get_amount_trades(start_cord,)
                            print(amount_trades, 'profit')
                            average = sum(amount_trades) / len(amount_trades)
                            if len(amount_trades) > 8 and average > 10:
                                pass

                            functions.mouse_move_click(start_cord[0] + exit_from_orders[0],
                                                       start_cord[1] + exit_from_orders[1])

                        functions.mouse_move(820, 370)
                        functions.mouse_click_and_move(820, 295)
                    else:
                        pass




                except Exception as e:
                    print(e)

        except Exception as e:
            print('error')