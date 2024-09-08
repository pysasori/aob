import time

import pyautogui
import cv2
import numpy


def checking_object_on_screen(img: str, threshold: float = 0.87, cords: list|None = None) -> bool | tuple[int, int]:
    img_rgb = cv2.imread(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    while True:
        if cords:
            #print('region', cords[0], cords[1], cords[2], cords[3])
            screen = pyautogui.screenshot(region=(int(cords[0]), int(cords[1]), int(cords[2]), int(cords[3])))
        else:
            screen = pyautogui.screenshot()
        screen = cv2.cvtColor(numpy.array(screen), cv2.COLOR_RGB2GRAY)
        # коорды
        w, h = img_gray.shape[::-1]
        res = cv2.matchTemplate(screen, img_gray, cv2.TM_CCOEFF_NORMED)

        loc = numpy.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (250, 0, 255), 1)
            print("find here ", (loc[1][0]), (loc[0][0]), w, h)
            cv2.imwrite('logs_screen/search_on_screen_found.png', screen)
            x = 2
            # получаемые знач
            if cords:
                x = (loc[1][0]) + cords[0]
                y = (loc[0][0]) + cords[1]
            else:
                x = (loc[1][0])
                y = (loc[0][0])
            return x, y
        return False
