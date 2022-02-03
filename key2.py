from pynput.keyboard import Key, Listener
import keyboard
import time
import os
import logging
logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(message)s')
while True:
    a = keyboard.read_event()     #Reading the key
    if a.name == "esc":break      #Loop will break on pressing esc, you can remove that
    elif a.event_type == "down":  #If any button is pressed (Not talking about released) then wait for it to be released
        t = time.time()           #Getting time in sec
        b = keyboard.read_event() 
        while not b.event_type == "up" and b.name == a.name:  #Loop till the key event doesn't matches the old one
            b = keyboard.read_event()
        logging.info(str(b.name)+"|"+str(time.time()-t))

