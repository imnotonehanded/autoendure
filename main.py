
import time
import os
import json
from pyautogui import *
import pyautogui
import keyboard
import random
import win32api, win32con

configFile = open("config.json")
config = json.load(configFile)
authKey = "ssd"
ssd = 0
prints= True
if config["print"] == "false": prints = False 
autoKey = config["autokey"]
zone = config["zone"]
zones = {"stonewood": "stone.png", "plankerton": "plank.png", "cannyvalley": "canny.png", "twinepeaks": "twine.png"}
zonepng= ""
if zones[zone]:
  zonepng = zones[zone]
else:
  print("Error: Invalid zone name check #faq for more info")

#W.I.P. will check through a database to make sure the key is correct
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


  loc0 = pyautogui.locateOnScreen('D:/autoendure-1/images/map.png', confidence = 0.8)
  if loc0 !=None:
    pyautogui.click(loc0)
  time.sleep(1)


  loc1 = pyautogui.locateOnScreen('D:/autoendure-1/images/'+zonepng, confidence = 0.8)
  if loc1 !=None:
    pyautogui.click(loc1)
    pyautogui.click(loc1)
    pyautogui.click(loc1)
  time.sleep(1)

  loc2 = pyautogui.locateOnScreen('D:/autoendure-1/images/ssd.png', confidence = 0.8)
  if loc2 !=None:
    pyautogui.click(loc2)
    pyautogui.click(loc2)
    pyautogui.click(loc2)
  time.sleep(0.5)
  

  loc3 = pyautogui.locateOnScreen('D:/autoendure-1/images/luanch.png', confidence = 0.8)
  if loc3 !=None:
    time.sleep(0.5)
    pyautogui.click(loc3)
    pyautogui.click(pyautogui.locateOnScreen('D:/autoendure-1/images/distract.png', confidence = 0.8))
    pyautogui.click(loc3)
    
  time.sleep(15)
  loc4 = pyautogui.locateOnScreen('D:/autoendure-1/images/luanch2.png', confidence = 0.8)
  if loc4 !=None:
    pyautogui.click(loc4)
  time.sleep(0.5)


  if prints: print("Luanched")
  time.sleep(0.5)


  if prints: print("Waiting for ssd to load in")
  time.sleep(0.5)


  #waits until ssdtext.png is not visible
  if prints: print("Walking to storm computer")
  #uses keystrokes to simulate keypresses, once ended press e, then after 1 second finds storm shield buttons and presses it then finds start and starts 


  if prints: print("Started, waiting for endurance to end")
  #every 10 seconds it waits to find the open buttons, presses it then presses collect all


  if prints: print("Collected Chest")
  #checks again if it can see open, if it does it opens then collect all, if it doesnt then it starts again


  start()
  

print("Welcome to AutoEndure by airttq")
time.sleep(.1)
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
    start()
  else:
    os.system("exit()")
else:
  print("Wrong Key!")
  os.system("exit()")