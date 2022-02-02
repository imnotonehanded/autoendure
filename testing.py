from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

loc0 = pyautogui.locateOnScreen('D:/autoendure-1/images/map.png', confidence = 0.8)
if loc0 !=None:
    print("seen")
    pyautogui.click(loc0)
    time.sleep(0.5)
else:
    print("not seen")
    time.sleep(0.5)
