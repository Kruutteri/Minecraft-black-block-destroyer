#Minecraft sensitivity 60%
import pyautogui,time,win32api,win32con,keyboard,random
from PIL import ImageGrab
from directkeys import PressKey, ReleaseKey, W, A, S, D

y_keski = round((1079/2))
x_keski = round((1919/2))

time.sleep(2)

minimi_x = 355
minimi_y = 255
screen = ImageGrab.grab(bbox=(355,255,425,278))

while True:        
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,x_keski,10000)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,x_keski,-840)

    time.sleep(0.1)

    x_max = round((1919/2)+1)
    x_min = round((1919/2)-1)

    x = x_min
    y = 0

    screen = ImageGrab.grab(bbox=(x_min,0,x_max,1000))

    alotusaika = time.time()
    while True:
        if keyboard.is_pressed("l"):
            exit()
        
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,x_keski-5,y_keski-32)
        if screen.getpixel((x-x_min,y)) == (0,0,0) and time.time()-alotusaika >= 1:
                print("x:",x,",","y:",y)
                block_y = y
                break

        y += 5
        
        if y >= 1000:
            y = 0
            x += 50
            screen = ImageGrab.grab(bbox=(x_min,0,x_max,1000))

        if x >= x_max:
            x = x_min


    time.sleep(0.1)
    #vitun kova funktio blokin etäisyyden laskemiseen y-koordinaatin avulla
    distance = (1.873*10**7)*10**(-0.01131*block_y)+2.169

    print(distance)

    #walking speed = 4.317 blocks/s
    v = 4.317

    aika = (distance-2)/v

    PressKey(W)
    time.sleep(aika)
    ReleaseKey(W)
    PressKey(S)
    ReleaseKey(S)

    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,x_keski,10000)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,x_keski,-450)
    time.sleep(0.1)

    #Tässä kohtaa mainaa blokki
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x_keski,y_keski-32,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x_keski,y_keski-32,0,0)
    time.sleep(0.1)

    #käännytään 180 astetta
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,x_keski,10000)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,x_keski,-840)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,-1738,y_keski-32)

    PressKey(W)
    time.sleep(aika)
    ReleaseKey(W)
    PressKey(S)
    ReleaseKey(S)


