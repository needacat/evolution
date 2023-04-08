import os
import time

import win32gui

from gamectl import *


class Simulator:
    def __init__(self, window_name: str):
        self.phwnd = 0
        self.chwnd = 0
        self.window_name = window_name

    def check_simulator_status(self):
        """检测模拟器是否开启"""
        # 句柄不为0则模拟器已开启
        if self.get_phwnd() != 0:
            return True
        else:
            return False

    def get_phwnd(self):
        """查找父窗口的句柄, 并存储到对象属性"""
        self.phwnd = win32gui.FindWindow(None, self.window_name)
        return self.phwnd

    def get_chwnd(self):
        """查找子窗口的句柄"""
        # self.chwnd =
        pass


