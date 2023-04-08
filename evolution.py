from simulator import *
from settings import *
from gamectl import *
from app import *


def enter_game(settings):
    _template = load_image(settings.template_path)
    _input = load_image(settings.icon_path)
    while not check_devices_status():
        continue
    time.sleep(4)

    while True:
        screen_capture()
        if match_template(_input, _template) is None or check_devices_status() == False:
            continue

        evo = App(settings)
        evo.start()
        break


def run():
    # 新建配置类对象
    settings = Settings()
    # 新建模拟器对象
    simulator = Simulator(settings.window_name)
    # simulator.get_phwnd()
    if not simulator.check_simulator_status():
        start_simulator(settings)

    enter_game(settings)

    # 主功能
    while True:
        screen_capture()

        pass


if __name__ == '__main__':
    run()
