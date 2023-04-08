from adb import *


class App:
    def __init__(self, settings):
        self.icon_path = settings.icon_path
        self.activity = r'com.tanyu.cjhwy/org.cocos2dx.javascript.SplashActivity'
        self.scene = {'开服公告': 'kfgg.png', '开始游戏': 'ksyx.png'}

    def start(self):
        start_activity(self.activity)
