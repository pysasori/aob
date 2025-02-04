import time

import functions
from config import *

def queue_12_hours ():

    # Устанавливаем значения по умолчанию, если переменных нет
    if 'SLEEP_QUEUE' not in globals():
        return True
    else:
        sleep_queue = SLEEP_QUEUE

    if 'MODE_QUEUE' not in globals():
        return True
    else:
        mode_queue = MODE_QUEUE

    if mode_queue is None or mode_queue not in [1, 2]:
        raise ValueError("mode_queue должен быть 1 или 2")

    # Текущее время (часы) в 24-часовом формате
    current_hour = time.localtime().tm_hour

    # Вычисляем стартовый час для интервала времени
    start_hour = sleep_queue  # Для каждого sleep_queue сдвиг на 1 час
    end_hour = (start_hour + 12) % 24  # Интервал в 12 часов, переход через 24

    # Проверяем, попадает ли текущее время в диапазон
    if start_hour <= current_hour < end_hour or (
            start_hour > end_hour and (current_hour >= start_hour or current_hour < end_hour)):
        # Если mode_queue = 1, возвращаем True, если в диапазоне времени
        if mode_queue == 1:
            return True
        # Если mode_queue = 2, возвращаем False, если в диапазоне времени
        else:
            functions.kill_process_by_window_name("Albion-Online.exe")
            time.sleep(2)
            functions.kill_process_by_window_name("AlbionLauncher.exe")
            time.sleep(2)
            functions.kill_process_by_window_name("Albion-Online_BE.exe")
            time.sleep(2)
            return False
    else:
        # Если текущее время не в диапазоне
        if mode_queue == 1:
            functions.kill_process_by_window_name("Albion-Online.exe")
            time.sleep(2)
            functions.kill_process_by_window_name("AlbionLauncher.exe")
            time.sleep(2)
            functions.kill_process_by_window_name("Albion-Online_BE.exe")
            time.sleep(2)
            return False
        else:
            return True



def queue_16_hours():
    # Устанавливаем значения по умолчанию, если переменных нет
    if 'SLEEP_QUEUE' not in globals():
        return True
    else:
        sleep_queue = SLEEP_QUEUE


    # Проверяем, что SLEEP_QUEUE в диапазоне от 0 до 12
    # if not (0 <= sleep_queue <= 12):
    #     raise ValueError("SLEEP_QUEUE должен быть в диапазоне от 0 до 12.")

    # Текущее время (часы) в 24-часовом формате
    current_hour = time.localtime().tm_hour

    # Вычисляем интервал для True и False
    start_hour = sleep_queue  # Стартовый час
    true_end_hour = (start_hour + 16) % 24  # Интервал True 16 часов
    #false_end_hour = (true_end_hour + 8) % 24  # Интервал False 8 часов

    # Проверяем, попадает ли текущее время в диапазон True (16 часов)
    if start_hour <= current_hour < true_end_hour or (start_hour > true_end_hour and (current_hour >= start_hour or current_hour < true_end_hour)):
        return True
    else:
        functions.kill_process_by_window_name("Albion-Online.exe")
        time.sleep(2)
        functions.kill_process_by_window_name("AlbionLauncher.exe")
        time.sleep(2)
        functions.kill_process_by_window_name("Albion-Online_BE.exe")
        time.sleep(2)
        return False

