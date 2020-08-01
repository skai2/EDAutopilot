from autopilot.control import keybinds
# The below imports should define which control module is used in all
# autopilot routines which should simply import autopilot.control
# (As long as they always implement the necessary send() and clear())
from autopilot.control.directinput.send import send
from autopilot.control.directinput.clear import clear