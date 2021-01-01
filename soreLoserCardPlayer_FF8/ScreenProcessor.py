import win32gui
import pygetwindow as gw
import numpy as np
import cv2, win32gui, time, math, win32con, win32ui
from PIL import ImageGrab, Image
import ctypes
import ctypes.wintypes
FINAL_FANTASY_WINDOW_TITLE = 'FINAL FANTASY VIII Remastered'
# Find FF8 game.

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

class ScreenProcessor:
    def __init__(self):
        self.window_rect = (0,) * 4

    def ff_get_screen_hwnd(self):
        window_hwnd = win32gui.FindWindow(0, FINAL_FANTASY_WINDOW_TITLE)
        if not window_hwnd:
            return 0
        else:
            return window_hwnd

    def ff_get_screen_rect(self, hwnd=None):
        """
        Added compatibility code from
        https://stackoverflow.com/questions/51786794/using-imagegrab-with-bbox-from-pywin32s-getwindowrect
        :param hwnd: window handle from self.ms_get_screen_hwnd
        :return: window rect (x1, y1, x2, y2) of FF rect.
        """
        try:
            f = ctypes.windll.dwmapi.DwmGetWindowAttribute
        except WindowsError:
            f = None
        if f:  # Vista & 7 stuff
            rect = ctypes.wintypes.RECT()
            DWMWA_EXTENDED_FRAME_BOUNDS = 9
            f(ctypes.wintypes.HWND(self.ff_get_screen_hwnd()),
              ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
              ctypes.byref(rect),
              ctypes.sizeof(rect)
              )
            size = (rect.left, rect.top, rect.right, rect.bottom)
        else:
            if not hwnd:
                hwnd = self.ff_get_screen_hwnd()
            self.window_rect = win32gui.GetWindowRect(hwnd)

        return size  # returns x1, y1, x2, y2

    def capture(self, set_focus=True, hwnd=None, rect=None):
        """Returns FF8 window screenshot handle(not np.array!)
        :param set_focus : True if MapleStory window is to be focusesd before capture, False if not
        :param hwnd : Default: None Win32API screen handle to use. If None, sets and uses self.hwnd
        :param rect : If defined, captures specificed ScreenRect area (x1, y1, x2, y2). Else, uses MS window ms_screen_rect.
        :return : returns Imagegrab of screen (PIL Image)"""
        if hwnd:
            self.hwnd = hwnd
        if not hwnd:
            self.hwnd = self.ff_get_screen_hwnd()
        if not rect:
            rect = self.ff_get_screen_rect(self.hwnd)

        img = ImageGrab.grab(rect)
        img = np.array(img)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # cv2.imwrite('image2.png', img)
        # cv2.imshow("Screen", img)
        # cv2.waitKey()
        return img


# ff_screen = ScreenProcessor()
#
# try:
#     ff = gw.getWindowsWithTitle(FINAL_FANTASY_WINDOW_TITLE)[0]  # Get window by name
#     # Bring window on top
#     ff.activate()
# except:
#     print("Can't find FF Client... Exiting")
#     exit(0)
#
# time.sleep(0.5)
# ff_screen.capture()
# ff_screen.ff_get_screen_rect()
