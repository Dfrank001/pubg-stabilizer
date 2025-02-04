import pynput.keyboard as keyboard
from pynput import mouse
from equipment import c_equipment,check,checkPosture
from mouse import *
from contants import  c_contants


#1，2选择武器
#num_lock开启关闭
#f12测试




def asyncHandle():
    if c_equipment.checkFlag:
        return
    c_contants.pool.submit(check)

def asyncHandlePosture():
    if c_equipment.checkPostureFlag:
        return
    c_contants.pool.submit(checkPosture)

# 键盘点击事件
def onRelease(key):
    try:
        if '1' == key.char:
            print("weapon 1")
            c_equipment.switch = 1
        elif '2' == key.char:
            print("weapon 2")
            c_equipment.switch = 2
        elif '3' == key.char:#手枪
            c_equipment.switch = 3
        elif '4' == key.char:#刀具
            c_equipment.switch = 3
        elif '5' == key.char:#手雷
            c_equipment.switch = 3
        elif 'c' == key.char or 'z' == key.char:
            asyncHandlePosture()
        #print("key char" + str(key.char))
    except AttributeError:
        if 'tab' == key.name:
            asyncHandle()
        elif 'f12' == key.name:
            testMouse()
        elif 'home' == key.name:
            changeOpen()
        elif 'shift' == key.name:
            c_contants.hold = False
        elif 'space' == key.name:
            asyncHandlePosture()
        #print("key name" + str(key.name))

def onPressed(key):
    try:
        if '1' == key.char:
            pass
    except AttributeError:
        if 'shift' == key.name:
            c_contants.hold = True

# 监听键盘
def listen_keybord():
    listener = keyboard.Listener(on_press=onPressed, on_release=onRelease)
    listener.start()


# 监听鼠标
def listen_mouse():
    with mouse.Listener(on_click=onClick) as listener:
        listener.join()


if __name__ == '__main__':
    listen_keybord()
    listen_mouse()