import time
import os
import json
from pyautogui import *
import pyautogui
import keyboard
import random
from pynput.keyboard import Key, Controller
import requests


keyboard = Controller()
configFile = open("D:/autoendure-1/config.json")
config = json.load(configFile)
authKey = "ssd"
ssd = 0
prints= True
if config["print"] == "false": prints = False 
autoKey = config["autokey"]
zone = config["zone"]
zones = {"stonewood": "stone", "plankerton": "plank", "cannyvalley": "canny", "twinepeaks": "twine"}
zonepng= ""
if zones[zone]:
  zonepng = zones[zone]
else:
  print("Error: Invalid zone name check #faq for more info")
def walk():
  macroFile = open('log.txt', 'r')
  for i in macroFile:
    i = i.split("|")
    a = i[0]
    b = i[1].replace("\n", "")
    press(a,float(b))
  macroFile.close()
def press(k,t):
  keyboard.press(k)
  time.sleep(t)
  keyboard.release(k)
def checkKey(key):
  if key == authKey:
    return True
  else:
    return False
def cls():
  os.system("cls")
  
#The main function 
def start():
  global ssd
  ssd+=1
  print('\033[2;32mStarted endurance '+str(ssd))

  #Clicks map
  while True:
    loc0 = pyautogui.locateOnScreen('D:/autoendure-1/images/map.png', confidence = 0.8)
    if loc0 != None:
      pyautogui.moveTo(loc0, duration=0.5, tween=pyautogui.easeInOutQuad)
      pyautogui.click(loc0)
      break
  time.sleep(1)

  #Clicks zone icon or large zone icon
  loc1 = pyautogui.locateOnScreen('D:/autoendure-1/images/'+zonepng + ".png", confidence = 0.8)
  locv1 = pyautogui.locateOnScreen('D:/autoendure-1/images/'+zonepng + "l" + ".png", confidence = 0.8)
  if loc1 !=None:
    pyautogui.click(loc1)
    pyautogui.click(loc1)
    pyautogui.click(loc1)
  elif locv1 != None:
    pyautogui.click(locv1)
    pyautogui.click(locv1)
    pyautogui.click(locv1)
  time.sleep(1)

  #Triple clicks the SSD Zone for next step
  loc2 = pyautogui.locateOnScreen('D:/autoendure-1/images/'+zonepng+'ssd.png', confidence = 0.8)
  pyautogui.click(loc2)
  pyautogui.click(loc2)
  pyautogui.click(loc2)
  time.sleep(0.5)
  
  #Moves mouse because of bug, luanches into main screen
  loc3 = pyautogui.locateOnScreen('D:/autoendure-1/images/luanch.png', confidence = 0.8)
  time.sleep(0.5)
  pyautogui.moveTo(loc3, duration=0.5, tween=pyautogui.easeInOutQuad)
  pyautogui.click(loc3)
  time.sleep(15)
  
  #Waits 15 seconds then luanches into the actual game
  while True:
    time.sleep(1)
    loc4 = pyautogui.locateOnScreen('D:/autoendure-1/images/luanch2.png', confidence = 0.8)
    if loc4 != None:
      pyautogui.moveTo(loc4, duration=0.5, tween=pyautogui.easeInOutQuad)
      pyautogui.click(loc4)
      break
  time.sleep(5)

  #Waits until it cant see the white dot, signifing that we're loaded in
  #while True:
  #  time.sleep(1)
  # l1c = pyautogui.locateOnScreen('D:/autoendure-1/images/temp1.png', confidence = 0.8)
  #  if  l1c == None:
  #    print("broken")
  #    break
  time.sleep(60)
  
  #Iterates through the file with all the keystrokes and clicks each one
  walk()
  time.sleep(0.5)
  press("e", 0)
  time.sleep(2)
  
  #Finds Start SSD button and clicks it
  while True:
    time.sleep(1)
    loc5 = pyautogui.locateOnScreen('D:/autoendure-1/images/ssde.png', confidence = 0.8)
    if loc5 != None:
      pyautogui.moveTo(loc5, duration=0.5, tween=pyautogui.easeInOutQuad)
      pyautogui.click(loc5)
      break
  time.sleep(0.5)
  
  #Clicks Start Endurance
  while True:
    time.sleep(1)
    loc6 = pyautogui.locateOnScreen('D:/autoendure-1/images/startssd.png', confidence = 0.8)
    if loc6 != None:
      pyautogui.moveTo(loc6, duration=0.5, tween=pyautogui.easeInOutQuad)
      pyautogui.click(loc6)
      break
  time.sleep(0.5)
  
  #Waits until it sees the Open button then breaks the while loop
  while True:
    if pyautogui.locateOnScreen('D:/autoendure-1/images/open.png', confidence = 0.8) != None:
      break
    else:
      time.sleep(5)
  
  #Finds open button clicks on it, then presses open all, then re loops until all things are opened
  while True:
    loc7 = pyautogui.locateOnScreen('D:/autoendure-1/images/open.png', confidence = 0.8)
    if loc7 != None:
      pyautogui.moveTo(loc7, duration=0.5, tween=pyautogui.easeInOutQuad)
      pyautogui.click(loc7)
      while True:
        loc8 = pyautogui.locateOnScreen('D:/autoendure-1/images/collectall.png', confidence = 0.8)
        if loc8 != None:
          pyautogui.moveTo(loc8, duration=0.5, tween=pyautogui.easeInOutQuad)
          pyautogui.click(loc8)
          time.sleep(2)
          break
    else:
      break
    
  #Sends to discord web hook
  data = {"content": 'Just finished endurance #'+str(ssd)}
  response = requests.post(config["webhook"], json=data)
  start()

print("Welcome to AutoEndure by airttq")
time.sleep(1)
cls()
print("\033[2;31mPress Ctrl+C to stop")
start()
