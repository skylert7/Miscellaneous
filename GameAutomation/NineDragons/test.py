import keyboard
import pyautogui
import time
def on_press_reaction(event):
    #https://stackoverflow.com/questions/47184374/increase-just-by-one-when-a-key-is-pressed/47184663
    if event.name == 'a':
        pyautogui.keyDown('s')
        pyautogui.keyUp('s')
    if event.name == 'd':
        keyboard.write('sai')


if __name__ == '__main__':
    keyboard.on_press(on_press_reaction)
    while True:
        print('',end='')