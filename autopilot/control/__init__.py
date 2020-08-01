from autopilot.control import keybinds
# The below import should define which control module is used in all
# autopilot routines which should simply import autopilot.control
# (As long as they always implement the necessary send() and clear())
from autopilot.control.directinput import send, clear