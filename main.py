import time
import os
import json
from pyautogui import *
import pyautogui
import keyboard
import random
from pynput.keyboard import Key, Controller
import requests

wasd = ["w", "a", "s", "d"]
macroFile = open('log.txt', 'r')
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
  loc0 = pyautogui.locateOnScreen('D:/autoendure-1/images/map.png', confidence = 0.8)
  pyautogui.click(loc0)
  print("hello?")
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
  loc4 = pyautogui.locateOnScreen('D:/autoendure-1/images/luanch2.png', confidence = 0.8)
  pyautogui.click(loc4)
  time.sleep(4)

  #Waits until it cant see the white dot, signifing that we're loaded in
  while True:
    time.sleep(1)
    if pyautogui.locateOnScreen('D:/autoendure-1/images/whitedot.png', confidence = 0.8):
      continue
    else:
      break
  time.sleep(2)
  
  #Iterates through the file with all the keystrokes and clicks each one
  for i in macroFile:
    i = i.split("|")
    a = i[0]
    b = i[1].replace("\n", "")
    press(a,float(b))
  time.sleep(0.5)
  press("e", 0)
  time.sleep(2)
  
  #Finds Start SSD button and clicks it
  loc5 = pyautogui.locateOnScreen('D:/autoendure-1/images/ssde.png', confidence = 0.8)
  pyautogui.moveTo(loc5, duration=0.5, tween=pyautogui.easeInOutQuad)
  pyautogui.click(loc5)
  time.sleep(0.5)
  
  #Clicks Start Endurance
  loc6 = pyautogui.locateOnScreen('D:/autoendure-1/images/startssd.png', confidence = 0.8)
  pyautogui.moveTo(loc6, duration=0.5, tween=pyautogui.easeInOutQuad)
  pyautogui.click(loc6)
  time.sleep(0.5)
  
  #Waits until it sees the Open button then breaks the while loop
  while True:
    if pyautogui.locateOnScreen('D:/autoendure-1/images/open.png', confidence = 0.8) != None:
      print("found")
      break
    else:
      time.sleep(5)
  
  #Finds open button clicks on it, then presses open all, then re loops until all things are opened
  while True:
    loc7 = pyautogui.locateOnScreen('D:/autoendure-1/images/open.png', confidence = 0.8)
    if loc7 != None:
      pyautogui.moveTo(loc7, duration=0.5, tween=pyautogui.easeInOutQuad)
      pyautogui.click(loc7)
      #loc8 = pyautogui.locateOnScreen('D:/autoendure-1/images/collectall.png', confidence = 0.8)
      #pyautogui.moveTo(loc8, duration=0.5, tween=pyautogui.easeInOutQuad)
      #pyautogui.click(loc8)
    else:
      break
    
  #Sends to discord web hook
  data = {"content": 'Just finished endurance #'+str(ssd)}
  response = requests.post(config["webhook"], json=data)
  time.sleep(4)
  

print("Welcome to AutoEndure by airttq")
time.sleep(1)
cls()

print("Enter key:")
enteredKey = ""
if autoKey != "no":
    #print(autoKey)
    enteredKey = autoKey
else:
    enteredKey = input()
if checkKey(enteredKey):
  print("""
  Remember:
  1. Make sure party is set to private, if not the endurance will be set up with wait for assistance
  2. Make sure that the config file is filled out with the zone, it will not work if it doesn't know what zone to load into
  3. Also make sure to have the macro file that has the keystrokes to walk to the storm sheild computer, if it doesnt go to the computer it can't start
  """)
  choice = input("Start? y/n: ")
  if str(choice) == "y":
    print(choice)
    cls()
    for i in reversed(range(2)):
      print("Starting in " + str(i+1))
      time.sleep(1)
      cls()
    print("\033[2;31mPress Ctrl+C to stop")
    while True:
      start()
  else:
    os.system("exit()")
else:
  print("Wrong Key!")
  os.system("exit()")
