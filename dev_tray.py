from pystray import Icon, MenuItem, Menu
from PIL import Image # big
from dev_autopilot import autopilot, resource_path
import kthread
import keyboard


def setup(icon):
    icon.visible = True

def exit_action():
    stop_action()
    icon.visible = False
    icon.stop()

def start_action():
    global thread
    if not thread:
        thread = kthread.KThread(target = autopilot, name = "EDAutopilot")
        thread.start()

def stop_action():
    global thread
    if thread:
        thread.terminate()
        thread = None

def tray():
    global icon, thread
    icon = None
    thread = None

    name = 'ED - Autopilot'
    icon = Icon(name=name, title=name)
    logo = Image.open(resource_path('src/logo.png'))
    icon.icon = logo

    icon.menu = Menu(
            MenuItem('Start', lambda : start_action()),
            MenuItem('Exit', lambda : exit_action()),
        )

    keyboard.add_hotkey('home', start_action)
    keyboard.add_hotkey('end', stop_action)

    icon.run(setup)

if __name__ == '__main__':
    tray()
