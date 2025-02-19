import time
import keyboard
import utils
import functions
from config import *
import random
from functions.random_delay import random_delay
from core import Interaction

# from lots import *

interaction = Interaction()

if __name__ == "__main__":
    try:
        if functions.pull_latest_code():
            functions.restart_program()
    except:
        pass
    while True:
        try:
            if not utils.queue_16_hours():
                print(f'Мы спим до {SLEEP_QUEUE} Смотрите другую очередь')
                time.sleep(180)
                continue

            start_cord = functions.search_on_screen('templates_img/icon_game.bmp')

            functions.mouse_move_click(start_cord[0] + default_shift_start[0], start_cord[1] + default_shift_start[1])

            while True:
                try:
                    if not utils.queue_16_hours():
                        print(f'Мы спим до {SLEEP_QUEUE} Смотрите другую очередь p2')
                        time.sleep(180)
                        break
                    amount_lots = utils.update_amount_lots(start_cord, list_towarow_main)

                    list_towarow = list_towarow_main[:amount_lots]

                    random.shuffle(list_towarow)

                    keyboard.press_and_release('esc')

                    # Activate auction
                    functions.mouse_move_click(start_cord[0] + NPC_CORDS[0], start_cord[1] + NPC_CORDS[1])
                    time.sleep(0.3)
                    back_row_cords = functions.search_on_screen(
                        'templates_img/back_row.bmp',
                        0.90,
                        [
                            start_cord[0],
                            start_cord[1],
                            len_window[0],
                            len_window[1]
                        ]
                    )
                    for item in list_towarow:
                        try:
                            print(len(list_towarow))
                            print(list_towarow.index(item))

                            ### Заходи в нужное меню продукта
                            #utils.choice_product(item, back_row_cords)
                            interaction.update_obj(item)
                            interaction.update_start_cords(start_cord)
                            interaction.update_back_row_cords(back_row_cords)


                            ### Получаем цены
                            sell_order, buy_order = interaction.go_to_orders_and_get_prices()
                            time.sleep(0.1)

                            profit = sell_order - buy_order
                            profit_percentage = (profit / sell_order)

                            if profit_percentage < item['profit']:
                                if profit_percentage < 13:
                                    utils.dell_first_buy_order(start_cord)
                                continue
                            if sell_order > 450000:
                                continue
                            #
                            # ### Количество ордеров покупок
                            # amount_buy = int(utils.amount_buy_items(start_cord))
                            # #print('amount_buy', amount_buy)
                            #
                            # ### Количество ордеров продажи
                            # amount_sell = int(utils.amount_sell_items(start_cord))
                            # #print('amount_sell', amount_sell)
                            #
                            #
                            # ### Проверка времени ласт ордера продажи
                            # buy_lust_time, sell_lust_time = utils.check_orders_lust_time(start_cord)
                            #
                            #
                            # try:
                            #     if amount_buy < 1 and amount_sell < 2:
                            #         utils.buy_lots(start_cord, buy_order)
                            #     elif amount_sell > 2:
                            #         utils.dell_first_buy_order(start_cord)
                            #     elif int(buy_lust_time) < (23 - int(item['time_update'])):
                            #         utils.dell_first_buy_order(start_cord)
                            #         utils.buy_lots(start_cord, buy_order)
                            # except Exception as e:
                            #     print(e, '86')
                            #
                            # try:
                            #     if int(sell_lust_time) < (23 - int(item['time_update'])):
                            #         utils.dell_first_sell_order(start_cord)
                            #         time.sleep(0.7)
                            #         ### Получаем товар в рюкзак если он есть
                            #         utils.lots_was_bought(start_cord)
                            #         time.sleep(0.6)
                            #
                            #         utils.choice_product(item, back_row_cords)
                            #         time.sleep(0.2)
                            #         utils.sell_lots(start_cord,sell_order)
                            #     random_delay()
                            #
                            # except Exception as e:
                            #     print(e, '103')

                            interaction.go_to_my_orders_and_work()

                            ### Получаем товар в рюкзак если он есть
                            utils.lots_was_bought(start_cord)
                            time.sleep(0.1)
                            random_delay()

                            ### BASE MODULE
                            utils.sell_and_buy_together(start_cord)

                        except Exception as e:
                            print(e, '113')
                            time.sleep(1)
                            keyboard.press_and_release('esc')
                            # Activate auction
                            functions.mouse_move_click(start_cord[0] + 691, start_cord[1] + 358)

                            #functions.mouse_move_click(start_cord[0] + auction_cord[0], start_cord[1] + auction_cord[1])
                            back_row_cords = functions.search_on_screen(
                                'templates_img/back_row.bmp',
                                0.90,
                                [
                                    start_cord[0],
                                    start_cord[1],
                                    len_window[0],
                                    len_window[1]
                                ]
                            )
                            time.sleep(1)
                            if not back_row_cords:
                                utils.custom_exception()


                except Exception as e:
                    print(e)
                    time.sleep(20)
                    utils.custom_exception()

        except Exception as e:
            print(e)
            time.sleep(20)
            utils.custom_exception()

