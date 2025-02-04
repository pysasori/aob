import functions
import utils
from bot.config import *
import time
import keyboard
import pyperclip



class Interaction:
    _instance = None  # Здесь хранится единственный экземпляр класса
    object = None
    back_row_cords = None
    start_cords = None
    sell_order = None
    buy_order = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.obj = None  # Инициализируем obj только один раз
        return cls._instance  # Возвращаем тот же объект

    def update_obj(self, obj):
        self.object = obj
        print('self.object', self.object)

    def update_back_row_cords(self, cords):
        self.back_row_cords = cords

    def update_start_cords(self, start_cords):
        self.start_cords = start_cords

    def choice_product(self):
        """
        Выбирает нужные пункты айтема
        """

        # Name
        functions.mouse_move_click(self.back_row_cords[0], self.back_row_cords[1])
        functions.mouse_long_click()
        time.sleep(0.1)
        functions.mouse_move_click(self.back_row_cords[0] - 80, self.back_row_cords[1])
        pyperclip.copy(self.object["object"])
        time.sleep(0.1)
        keyboard.press_and_release('ctrl + v')

        # Tier
        functions.mouse_move_click(self.back_row_cords[0] + 230, self.back_row_cords[1] + 11)
        functions.mouse_move_from_point(y=25 * (tier[self.object["tier"]] + 1))
        functions.mouse_click()

        # Enchantment
        functions.mouse_move_click(self.back_row_cords[0] + 380, self.back_row_cords[1] + 11)
        functions.mouse_move_from_point(y=25 * (enchantment[self.object["enchantment"]] + 1))
        functions.mouse_click()

    def delete_choice_product(self):
        functions.mouse_move_click(self.back_row_cords[0], self.back_row_cords[1])
        functions.mouse_long_click()
        time.sleep(0.2)
        functions.mouse_move_click(self.back_row_cords[0] + 566, self.back_row_cords[1])
        functions.mouse_long_click()

    def get_price(self):
        sell_order, buy_order = utils.scan_price(self.start_cords)
        functions.mouse_move_click(self.start_cords[0] + exit_from_orders[0], self.start_cords[1] + exit_from_orders[1])
        self.sell_order = sell_order
        self.buy_order = buy_order

    def sell_lot(self):
        functions.mouse_move_click(self.start_cords[0] + my_sell[0], self.start_cords[1] + my_sell[1])
        self.choice_product()
        utils.sell_lots(self.start_cords, self.sell_order)

    def go_to_orders_and_get_prices(self):
        time.sleep(0.3)
        functions.mouse_move_click(
            self.start_cords[0] + create_orders[0],
            self.start_cords[1] + create_orders[1]
        )  # go to orders
        time.sleep(0.1)

        self.choice_product()

        functions.mouse_move_click(
            self.start_cords[0] + btn_create_order[0],
            self.start_cords[1] + btn_create_order[1]
        )  # go to menu orders
        pull_out_menu = functions.checking_object_on_screen(
            'templates_img/pull_out_menu.bmp',
            0.90,
            [
                self.start_cords[0],
                self.start_cords[1],
                len_window[0],
                len_window[1]
            ]
        )
        if pull_out_menu:
            functions.mouse_move_click(pull_out_menu[0], pull_out_menu[1])

        self.get_price()

        return self.sell_order, self.buy_order

    def go_to_my_orders_and_work(self):
        time.sleep(0.3)
        # Переходим в мои ордера
        functions.mouse_move_click(
            self.start_cords[0] + my_orders[0],
            self.start_cords[1] + my_orders[1]
        )
        time.sleep(0.1)
        # Выбираем нужный продукт
        self.choice_product()

        amount_buy = utils.amount_buy_items(self.start_cords)
        amount_sell = utils.amount_sell_items(self.start_cords)
        buy_lust_time, sell_lust_time = utils.check_orders_lust_time(self.start_cords)
        # Условия отмены/изменения ордеров
        try:
            if amount_buy < 1 and amount_sell < 2:
                utils.buy_lots(self.start_cords, self.buy_order)
            elif amount_sell > 2:
                utils.dell_first_buy_order(self.start_cords)
            elif int(buy_lust_time) < (23 - int(self.object['time_update'])):
                utils.dell_first_buy_order(self.start_cords)
                utils.buy_lots(self.start_cords, self.buy_order)
        except Exception as e:
            print(e, '1 go_to_my_orders_and_work')
        try:
            if int(sell_lust_time) < (23 - int(self.object['time_update'])):
                utils.dell_first_sell_order(self.start_cords)
                time.sleep(0.7)
                ### Получаем товар в рюкзак если он есть
                utils.lots_was_bought(self.start_cords)
                time.sleep(0.6)
                self.sell_lot()
            time.sleep(0.2)

        except Exception as e:
            print(e, '2 go_to_my_orders_and_work')

