from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

# to get the position for the mouse (the values can be different on different screens )
def get_poz():
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        print('\b' * len(positionStr), end='', flush=True)
    print('\n')


# Tile 1 : Pozition X: 355,Y: 505
# Tile 2 : Pozition X: 448,Y: 505
# Tile 3 : Pozition X: 541,Y: 505
# Tile 4 : Pozition X: 631,Y: 505
# reload current page : Pozition X: 96,Y: 52
# play start : Pozition X: 491,Y: 442
# play game button : Pozition X: 493,Y: 454

# pyautogui.click(x, y) - move mouse to xy coord and click
# pyautogui.press('esc') - press the esc key


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)#pause the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# press q to stop the bot
def click_tiels():
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(355, 505)[0] == 0:
            click(355, 505)
        if pyautogui.pixel(448, 505)[0] == 0:
            click(448, 505)
        if pyautogui.pixel(541, 505)[0] == 0:
            click(541, 505)
        if pyautogui.pixel(631, 505)[0] == 0:
            click(631, 505)


pyautogui.click(96, 52)#reload page
time.sleep(1)
pyautogui.click(491, 442)#play start
time.sleep(1)
pyautogui.click(493, 454)#play game button
time.sleep(1)
click_tiels()

# get_poz()
