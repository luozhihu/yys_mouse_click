import win32api
import win32con
import win32gui
import time
import threading
import random
import inspect
import ctypes


a = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
b = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)


def MouseMove(x, y):  # 移动鼠标的位置
    win32api.SetCursorPos((x, y))


def MouseClick(x=None, y=None):  # 鼠标点击指定的地方
    if not x is None and not y is None:
        MouseMove(x, y)
        time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(random.uniform(0.001, 0.02))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def GetMousePosition():  # 得到鼠标的位置
    return win32api.GetCursorPos()


def GetWindowHwnd():
    X, Y = GetMousePosition()
    hwnd_value = win32gui.WindowFromPoint((X, Y))
    return hwnd_value


def WaitTime(x):
    time.sleep(random.uniform(0.1, 0.5)*x)


def WaitTime_short(x):
    time.sleep(random.uniform(0.02, 0.05)*x)


def WaitTime_wait(x):
    # if type(x) != "str"
    if isinstance(x, int):
        time.sleep(x)
    else:
        time.sleep(int(x))


class MyWindows:  # 新建一个窗口类
    def __init__(self, hwnd):
        self.hwnd = hwnd
        # 点击挑战的时候的位置坐标 坐标为组队的时候
        self.random_x_fight = random.uniform(0.92, 0.95)
        self.random_y_fight = random.uniform(0.84, 0.90)
        self.random_x_other = random.uniform(0.7, 0.74)
        self.random_y_other = random.uniform(0.75, 0.76)
        self.random_x_YuLing = random.uniform(0.84, 0.88)
        self.random_y_YuLing = random.uniform(0.86, 0.88)
        self.random_Wx_select = None
        self.random_Wy_select = None
        self.random_Wx_other_select = None
        self.random_Wy_other_select = None
    def GetWindowsRect(self):  # 更新窗口位置的大小并返回出

        self.left, self.top, self.right, self.bottom = win32gui.GetWindowRect(
            self.hwnd)
    def checkWindows(self):
        hwnd_return = win32gui.GetWindowText(self.hwnd)
        if hwnd_return == "阴阳师-网易游戏":
            self.GetWindowsRect()
        else:
            return 1
        return 0
    def ChangeWindows(self, left, top, width, hight):  # 改变窗口的位置
        hwnd_return = win32gui.GetWindowText(self.hwnd)
        if hwnd_return == "阴阳师-网易游戏":
            win32gui.MoveWindow(self.hwnd, left, top, width,
                                hight, True)  # 改变应用的位置和大小
            self.GetWindowsRect()
        else:
            return 1
        return 0

    def WindowsMoveClick(self, random_x, random_y):
        MouseClick(int((self.right-self.left)*random_x)+self.left,
                   int((self.bottom-self.top)*random_y)+self.top)

    def WindowsClickFight(self):
        self.random_x_fight = random.uniform(0.92, 0.97)
        self.random_y_fight = random.uniform(0.84, 0.92)
        self.WindowsMoveClick(self.random_x_fight, self.random_y_fight)

    def WindowsClickOther(self):
        self.random_x_other = random.uniform(0.7, 0.74)
        self.random_y_other = random.uniform(0.75, 0.76)
        self.WindowsMoveClick(self.random_x_other, self.random_y_other)

    def WindowsClickSelectFight(self):
        MouseClick(self.random_Wx_select+random.randint(-5, 5),
                   self.random_Wy_select+random.randint(-5, 5))

    def WindowsClickSelectOther(self):
        MouseClick(self.random_Wx_other_select+random.randint(-5, 5),
                   self.random_Wy_other_select+random.randint(-5, 5))

def turn_two(class1, class2):
    class1.WindowsClickOther()
    class1.WindowsClickOther()
    WaitTime(2)
    class2.WindowsClickOther()
    class2.WindowsClickOther()
    WaitTime(2)

def turnOneSelect(class1):
    class1.WindowsClickSelectOther()
    WaitTime(1)

def snake_two(class1, class2, num, times):

    WaitTime_wait(1)
    if num == "1":
        class1.WindowsClickFight()
    elif num == "2":
        class2.WindowsClickFight()
    WaitTime_wait(times)
    turn_two(class1, class2)
    WaitTime_short(3)
    turn_two(class1, class2)
    WaitTime_short(4)
    turn_two(class1, class2)
    WaitTime_short(2)
    turn_two(class1, class2)
    WaitTime_short(2)
    turn_two(class1, class2)

def selectOne(class1,times):
    WaitTime_wait(1)
    class1.WindowsClickSelectFight()
    WaitTime_wait(times)
    class1.WindowsClickSelectOther()
    WaitTime_short(20)
    class1.WindowsClickSelectOther()
    WaitTime_short(22)
    class1.WindowsClickSelectOther()
    WaitTime_short(22)
    class1.WindowsClickSelectOther()
    WaitTime_short(40)
    class1.WindowsClickSelectOther()
    WaitTime_short(4)
'''
def yuling_single():
    time.sleep(1)
    mouse_click(860,random.randint(458,478))
    time.sleep(70)
    mouse_click(550,random.randint(479,500))
    time.sleep(1)
    mouse_click(550, random.randint(479,500))
    time.sleep(1)
    mouse_click(550, random.randint(479,500))
    time.sleep(1)
def yuling_trouble():
    time.sleep(5)
    while 1:
        time.sleep(1)
        mouse_click(855,random.randint(984,1000))
        time.sleep(80)
        mouse_click(random.randint(527,653),999)
        time.sleep(1)
        mouse_click(random.randint(527,653),999)
        time.sleep(1)
        mouse_click(random.randint(527,653),999)
        time.sleep(1)


def yuling3():
    time.sleep(45)
    while 1:
        time.sleep(1)
        mouse_click(1729,random.randint(957,985))
        time.sleep(85)
        mouse_click(random.randint(1427,1553),979)
        time.sleep(1)
        mouse_click(random.randint(1427,1553),979)
        time.sleep(1)
        mouse_click(random.randint(1427,1553),979)
        time.sleep(1)
def turn_three():
    mouse_click(550, random.randint(400, 450))
    time.sleep(random.uniform(0.1, 0.5))
    mouse_click(random.randint(527, 653), 999)
    time.sleep(random.uniform(0.1, 0.5))
    mouse_click(random.randint(1427, 1553), 979)
    time.sleep(random.uniform(0.1, 0.5))
def three_snake_11():
    while 1:
        mouse_click(1729, random.randint(957, 985))
        time.sleep(80)
        turn_three()
        time.sleep(1)
        turn_three()
        time.sleep(1)
        turn_three()
        time.sleep(1)
        turn_three()
        time.sleep(3)

def turn_two():
    mouse_click(random.randint(400, 450),400)
    time.sleep(random.uniform(0.1, 0.5))
    mouse_click(random.randint(527, 653), 930)
    time.sleep(random.uniform(0.1, 0.5))
def two_snake_11():
    while 1:
        turn_two()
        time.sleep(3)
        mouse_click( random.randint(879, 889),random.randint(445, 456))
        time.sleep(50)
        turn_two()
        time.sleep(1)
        turn_two()
        time.sleep(1)
        turn_two()
        time.sleep(1)



#mouse_click(1729, random.randint(957, 985))
#yuling1()
#yuling1()
#get_position()
#yuling()
#print(s)
#three_snake_11()
#two_snake_11()

print(x)
print(y)
mouse_move(331,818)
while 1:
    mouse_click(331, 798)
    time.sleep(3)
    print(1)



# 每隔10秒钟执行
def t2():
    yuling1()
if __name__ == '__main__':
    t = threading.Thread(target=t2)
   # v = threading.Thread(target=yuling3)
    t.start()
    #v.start()
    yuling2()
    t.join()
    #v.join()
'''


#BO = BasicOption
# BO.mouse_click(855,random.randint(984,1000))


'''

class GetWindows():
    def __init__(self):
        self.spying = False

    def mouseMoveEvent(self):
        curX, curY = win32gui.GetCursorPos()
        hwnd = win32gui.WindowFromPoint((curX, curY))
        print(hwnd)
        time.sleep(0.2)


#wind = GetWindows()
#while(1):
#    wind.mouseMoveEvent()


'''


def stop_thread(thread, exctype=SystemExit):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(thread.ident)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
