import random
import keyboard
import pyautogui
import time
#IMPORT THE HELL OUT OF THE CODE HAHHAHAHAHAHHA

keysss=['up','down','left','right']
#This can be changed according to the emulator settings
def loop():

    for x in range(3):
        sus=random.choice(keysss)
        #sussy
        pyautogui.keyDown('x')
        #change the x here with whatever key you have for b or running so that you can run and move(saves time lol)
        pyautogui.keyDown(sus)
        pyautogui.keyUp(sus)
        pyautogui.keyUp('x')

def z():
    for x in range(4):
        pyautogui.keyDown('z')
        #Change this to the a key of your emulator i.e. the key that interacts with the env
        #You can check the name of keys in pyautogui that work with print(pyautogui.KEY_NAMES)
        time.sleep(0.2)
        pyautogui.keyDown('z')
        
        pyautogui.keyUp('z')
        time.sleep(0.2)
        
        pyautogui.keyUp('z')
        time.sleep(3.5)
        pyautogui.keyDown('z')
        time.sleep(0.2)
        pyautogui.keyDown('z')
        time.sleep(0.2)
        pyautogui.keyUp('z')
        time.sleep(0.2)
        pyautogui.keyUp('z')
    
#Change the keys according to ur wish
keyboard.add_hotkey('/',lambda:loop())
keyboard.add_hotkey(',',lambda:z())
input()
