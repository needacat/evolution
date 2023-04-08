import subprocess
import time


def check_devices_status():
    """检查adb连接情况，成功返回True"""
    _cmd = ['adb', 'devices', '-l']
    _devices_status = subprocess.run(_cmd, shell=True, capture_output=True)
    # 在返回结果中查找关键词
    if _devices_status.stdout.decode('GBK').find('SM_G955N') != -1 \
            and _devices_status.stdout.decode('GBK').find('offline') == -1:

        return True
    else:
        return False


def screen_capture(save_path='resource'):
    """通过adb截图并拷贝到save_path"""
    _sc_cmd = 'adb shell screencap /sdcard/sc.png'
    # 使用subprocess.check_output能够获得输出
    subprocess.run(_sc_cmd, shell=True)
    _pull_cmd = 'adb pull /sdcard/sc.png {}'.format(save_path)
    subprocess.run(_pull_cmd, shell=True)
    # 保证命令执行完毕
    time.sleep(0.1)


def start_activity(activity: str):
    _cmd = r'adb shell am start ' + activity
    subprocess.run(_cmd, shell=True)


def tap_loc(x: int, y: int):
    """点击坐标"""
    _cmd = 'adb shell input tap {} {}'.format(x, y)
    subprocess.run(_cmd, shell=True)
    time.sleep(0.1)


def press(key):
    """按下按键"""
    _cmd = 'adb shell input keyevent {}'.format(key)
    subprocess.run(_cmd, shell=True)
    time.sleep(0.1)


if __name__ == '__main__':
    screen_capture()
