from pynput.keyboard import Key , Controller
import time
import AI


keyboard = Controller()

def keybod(cmd):
    if "type" in cmd and "mode" in cmd:
        AI.speak("enabling type mode")
        while True:
            cmd=AI.myCommand()
            if 'disable type mode' in cmd:
                AI.speak("completed sir or not")
                break
            else:
                time.sleep(0.1)
                keyboard.type(cmd)
    elif "select all" in cmd:
        time.sleep(0.1)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('a')
            keyboard.release('a')
    elif "copy" in cmd:
        time.sleep(0.1)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
    elif "paste" in cmd:
        time.sleep(0.1)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
    elif "close" in cmd:
        time.sleep(0.1)
        with keyboard.pressed(Key.alt):
            keyboard.press(Key.f4)
            keyboard.release(Key.f4)
        '''AI.speak("save it or not")
        cmd = AI.myCommand()
        if cmd == 'save':
            keyboard.press(Key.enter)
            keyboard.press(Key.enter)
            AI.speak("by what name")
            cmd=AI.myCommand()
            keyboard.type(cmd)
            keyboard.press(Key.enter)
            keyboard.press(Key.enter)
            keyboard.type(cmd)
        elif "don't save" in cmd:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            keyboard.press(Key.enter)
            keyboard.press(Key.enter)
        else:
            pass'''
    elif "enter" in cmd:
        time.sleep(0.1)
        keyboard.press(Key.enter)
        keyboard.press(Key.enter)
            




