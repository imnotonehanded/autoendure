import time, keyboard
macroFile = open('log.txt', 'r')
def press(k,t):
  keyboard.press(k)
  time.sleep(t)
  keyboard.release(k)
for i in macroFile:
    i = i.split("|")
    a = i[0]
    b = i[1].replace("\n", "")
    press(a,float(b))