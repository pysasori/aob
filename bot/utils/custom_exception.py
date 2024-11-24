import time

import keyboard

import bot.functions as functions


from functions.random_delay import random_delay


def custom_exception():
    start_time = time.time()
    while True:
        functions.kill_process_by_window_name("Albion-Online.exe")
        time.sleep(2)
        functions.kill_process_by_window_name("AlbionLauncher.exe")
        time.sleep(2)
        functions.kill_process_by_window_name("Albion-Online_BE.exe")
        time.sleep(10)

        keyboard.press('win')
        time.sleep(0.1)
        keyboard.press_and_release('1')
        time.sleep(0.1)
        keyboard.release('win')

        time.sleep(30)
        play = functions.checking_object_on_screen('templates_img/play.bmp')
        if play:
            functions.mouse_move_click(play[0], play[1])
            time.sleep(180)
        else:
            settings = functions.checking_object_on_screen('templates_img/launch_settings.bmp')
            if not settings:
                functions.error_message_tg()
            else:
                functions.mouse_move_click(settings[0]+100, settings[1])
                time.sleep(180)

        enter_world = functions.checking_object_on_screen('templates_img/enter_world.bmp')
        if enter_world:
            functions.mouse_move_click(enter_world[0] + 100, enter_world[1])
            time.sleep(40)
            break
        if time.time() - start_time > 3600:
            functions.error_message_tg()
            time.sleep(600)












