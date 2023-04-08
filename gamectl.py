import cv2
import subprocess

import key
from adb import *


def start_simulator(settings):
    """启动模拟器"""
    _cmd = r'start /b ' + settings.simulator_path
    subprocess.run(_cmd, shell=True)


def load_image(image_path):
    """加载图片，返回对应numpy数组"""
    # [:, :, :3] 用于剔除alpha通道
    if cv2.imread(image_path) is None:
        press('-------------')
    return cv2.imread(image_path)[:, :, :3]


def match_template(input_, template):
    """
    :param input_: numpy数组
    :param template: numpy数组
    :return: 成功返回匹配坐标，失败返回None
    """
    _input_gray = cv2.cvtColor(input_, cv2.COLOR_BGR2GRAY)
    _template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    # 将模板大小调整到一半
    _template_gray = cv2.resize(_template_gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    _input_gray = cv2.resize(_input_gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    # 进行匹配
    result = cv2.matchTemplate(_input_gray, _template_gray, cv2.TM_CCOEFF_NORMED)
    _, _max_val, _, _max_loc = cv2.minMaxLoc(result)
    # 输出匹配度
    print('匹配度: {:.2f}'.format(_max_val))
    if _max_val >= 0.9:
        _client_x, _client_y = _max_loc
        # 恢复正常大小坐标
        return _client_x * 2, _client_y * 2
    else:
        return None


def announcement():
    """检测页面若为公告，则点击返回按钮关闭公告"""
    screen_capture()
    _template = load_image(r'resource\sc.png')
    _input = load_image(r'resource\kfgg.png')

    if match_template(_input, _template) is not None:
        press(key.BACK)


def start_game():
    """点击开始游戏"""
