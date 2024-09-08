import pyautogui
import pytesseract
import cv2
import numpy as np
from PIL import Image


def scan_prices(cords: list | None = None) -> str:
    if cords:
        screen = pyautogui.screenshot(region=(int(cords[0]), int(cords[1]), int(cords[2]), int(cords[3])))
    else:
        screen = pyautogui.screenshot()
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = Image.frombytes('RGB', screen.size, screen.tobytes())

    # Преобразуем объект Image в массив NumPy
    image = np.array(image)
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=1.3, tileGridSize=(2, 2))
    image = clahe.apply(image)

    # второй вариант конвертирование изображение в чб вариант для тесракта(рабочий)

    # image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # thresh = 55 #64 #55
    # image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite('logs_screen/prices.png', image)

    string = pytesseract.image_to_string(image, config=' --psm 6 --oem 3 -c tessedit_char_whitelist=0123456789,')
    print(string)
    return string



#
# def scan_prices(cords: list | None = None) -> str:
#     if cords:
#         screen = pyautogui.screenshot(region=(int(cords[0]), int(cords[1]), int(cords[2]), int(cords[3])))
#     else:
#         screen = pyautogui.screenshot()
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#     image = Image.frombytes('RGB', screen.size, screen.tobytes())
#
#     # Преобразуем объект Image в массив NumPy
#     image = np.array(image)
#     image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(2, 2))
#     image = clahe.apply(image)
#
#     # второй вариант конвертирование изображение в чб вариант для тесракта(рабочий)
#
#     # image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
#     # thresh = 55 #64 #55
#     # image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]
#
#     cv2.imwrite('logs_screen/prices.png', image)
#
#     string = pytesseract.image_to_string(image, config=' --psm 6 --oem 3 -c tessedit_char_whitelist=0123456789,')
#     print(string)
#     return string
