from pynput import mouse
import os
import pyautogui
import time
import random
import pyperclip
import pygetwindow as gw
a=[0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,2]
''' while True: #偵測當前滑鼠位置
    print(pyautogui.position())
    time.sleep(0.1) '''
#pyautogui.hotkey('win','down') #自動使視窗最小化
#os.system('mode 13,2')
window_title = "C:\Windows\py.exe"
cmd_window = gw.getWindowsWithTitle(window_title)
if cmd_window:
    cmd_window[0].left = -10
    cmd_window[0].top = -1
    cmd_window[0].width = 190
    cmd_window[0].height = 90 #設定cmd視窗大小
def on_click(x, y, button, pressed):
    if not pressed:
        # Stop listener
        return False
for i in range(1):
    with mouse.Listener(on_click=on_click) as listener:listener.join()
    listener = mouse.Listener(on_click=on_click)
    listener.start()
pos=pyautogui.position()
xp=pos.x+35
xm=pos.x-35
yp=pos.y+35
ym=pos.y-35
count=0
while True: #迴圈執行複製貼上發送動作
    pos=pyautogui.position()
    if pos.x>xp or pos.x<xm or pos.y>yp or pos.y<ym:
        break
    x=u'\u270A'
    pyperclip.copy(x)
    pyautogui.hotkey('ctrl','v')
    pyautogui.click()
    os.system("cls")
    count+=1
    print('count:',count)
    time.sleep(random.choice(a)) #隨機選取時間避免偵測