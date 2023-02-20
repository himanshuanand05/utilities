import pyautogui
import threading
import random

def move():
    rnum = random.randint(200,500)
    print(rnum)
    threading.Timer(rnum, move).start()
    rnum = random.randint(-100,100)
    pyautogui.moveRel(rnum, rnum, duration=1)
    print(rnum)
    pyautogui.hotkey('alt','tab')
    if(1):
        pyautogui.keyDown('ctrl')
        rnum = random.randint(1,6)
        while rnum > 0:
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')
            rnum = rnum - 1 

        pyautogui.keyUp('ctrl')

move()
