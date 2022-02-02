from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)
loc3 = pyautogui.locateOnScreen('D:/autoendure-1/images/luanch.png', confidence = 0.8)
pyautogui.moveTo(loc3, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click(loc3)