import time
import pyautogui
pyautogui.FAILSAFE = False
from functions.random_delay import random_delay


def mouse_move(x=None, y=None, t=0.5):
    if x and y:
        pyautogui.moveTo(x, y, t)
    elif x:
        current_position = pyautogui.position()
        pyautogui.moveTo(x, current_position.y, t)
    elif y:
        current_position = pyautogui.position()
        pyautogui.moveTo(current_position.x, y, t)
    random_delay()


def mouse_move_from_point(x=None, y=None, t=0.5):
    current_position = pyautogui.position()
    if x and y:
        pyautogui.moveTo(x + current_position.x, y + current_position.y, t)
    elif x:
        pyautogui.moveTo(x + current_position.x, current_position.y, t)
    elif y:
        pyautogui.moveTo(current_position.x, y + current_position.y, t)
    random_delay()


def mouse_move_click(x=None, y=None, t=0.2):
    if x and y:
        pyautogui.moveTo(x, y, t)
    elif x:
        current_position = pyautogui.position()
        pyautogui.moveTo(x, current_position.y, t)
    elif y:
        current_position = pyautogui.position()
        pyautogui.moveTo(current_position.x, y, t)
    random_delay()
    pyautogui.click()
    random_delay()


def mouse_move_click_left(x=None, y=None, t=0.5):
    pyautogui.dragTo(x, y, t, button='left')


def mouse_click(*kords):
    random_delay()
    if kords:
        pyautogui.click(kords[0], kords[1])
    else:
        pyautogui.click()
    random_delay()

# MINUS
def mouse_click_and_move(x, y, t=1.5):
    random_delay()
    pyautogui.dragTo(x, y, t, button='left')
    random_delay()


def mouse_long_click(t=0.2):
    current_position = pyautogui.position()
    random_delay()
    pyautogui.dragTo(current_position.x, current_position.y, t, button='left')
    random_delay()


# MINUS
def mouse_scroll(px):
    # Зажимаем правую клавишу мыши
    pyautogui.mouseDown(button='right')

    # Сдвигаем мышь на 50 пикселей вниз
    pyautogui.move(0, -px, duration=1)

    # Отпускаем правую клавишу мыши
    pyautogui.mouseUp(button='right')

    # Сдвигаем мышь на 50 пикселей вниз
    pyautogui.move(0, px, duration=1)


