```python
import pyautogui as pg
import time
from PIL import ImageGrab
import keyboard

taps = [(321,788),(414,788),(507,788),(598,788)]
state = False
width, height = pg.size() # 전체 사이즈.
box = (0,0, width/2, height)    # 사이즈를 반으로 줄여 속도를 높인다.

def play():
    screen = ImageGrab.grab(box)    # 화면 반으로 줄어들게 함.
    for tap in taps:
        if (0, 0, 0) == screen.getpixel(tap):   # (0, 0, 0)은 검정색 (255, 255, 255)는 흰색
            pg.click(*tap)  # '*' 요건 언패킹 연산자 '()' 바깥 괄호를 없애줌.
                            # (tap[0],tap[1]) 요거랑 (*tap)는 같다.
while True:
    if not state and keyboard.is_pressed('a'):
        state = True
        print("Start!")
    elif state and keyboard.is_pressed('s'):
        state = False
        print("Stop!")
    if state:
        play()
    # print(pg.position()) 화면 상의 taps 위치 찾아준 기능.
    # time.sleep(.5)
```

> http://zzzscore.com/dontap/ 에서 해당 위치의 색깔이 바뀔 때 마다 클릭을 해주는 코드.