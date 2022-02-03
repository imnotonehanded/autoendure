import time
import pyautogui
import keyboard
while True:
    time.sleep(2)
    if pyautogui.locateOnScreen('D:/autoendure-1/images/open.png', confidence = 0.8) != None:
      print("seen")
    else:
      print("nope")