#!/usr/bin/env python
# coding: utf-8

# <h1>Elite Dangerous Autopilot v2<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#References" data-toc-modified-id="References-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Constants" data-toc-modified-id="Constants-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Constants</a></span></li><li><span><a href="#Read-ED-logs" data-toc-modified-id="Read-ED-logs-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Read ED logs</a></span><ul class="toc-item"><li><span><a href="#Get-latest-log-file" data-toc-modified-id="Get-latest-log-file-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Get latest log file</a></span></li><li><span><a href="#Extract-ship-info-from-log" data-toc-modified-id="Extract-ship-info-from-log-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Extract ship info from log</a></span></li></ul></li><li><span><a href="#Control-ED-with-direct-input" data-toc-modified-id="Control-ED-with-direct-input-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Control ED with direct input</a></span><ul class="toc-item"><li><span><a href="#Get-necessary-keybinds" data-toc-modified-id="Get-necessary-keybinds-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Get necessary keybinds</a></span></li></ul></li><li><span><a href="#Direct-input-function" data-toc-modified-id="Direct-input-function-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Direct input function</a></span></li><li><span><a href="#OpenCV" data-toc-modified-id="OpenCV-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>OpenCV</a></span><ul class="toc-item"><li><span><a href="#Get-screen" data-toc-modified-id="Get-screen-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Get screen</a></span></li><li><span><a href="#HSV-slider-tool" data-toc-modified-id="HSV-slider-tool-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>HSV slider tool</a></span></li><li><span><a href="#Filter-sun" data-toc-modified-id="Filter-sun-7.3"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>Filter sun</a></span></li><li><span><a href="#Filter-orange" data-toc-modified-id="Filter-orange-7.4"><span class="toc-item-num">7.4&nbsp;&nbsp;</span>Filter orange</a></span></li><li><span><a href="#Filter-orange2" data-toc-modified-id="Filter-orange2-7.5"><span class="toc-item-num">7.5&nbsp;&nbsp;</span>Filter orange2</a></span></li><li><span><a href="#Filter-blue" data-toc-modified-id="Filter-blue-7.6"><span class="toc-item-num">7.6&nbsp;&nbsp;</span>Filter blue</a></span></li><li><span><a href="#Get-sun" data-toc-modified-id="Get-sun-7.7"><span class="toc-item-num">7.7&nbsp;&nbsp;</span>Get sun</a></span></li><li><span><a href="#Get-compass-image" data-toc-modified-id="Get-compass-image-7.8"><span class="toc-item-num">7.8&nbsp;&nbsp;</span>Get compass image</a></span></li><li><span><a href="#Get-navpoint-offset" data-toc-modified-id="Get-navpoint-offset-7.9"><span class="toc-item-num">7.9&nbsp;&nbsp;</span>Get navpoint offset</a></span></li><li><span><a href="#Get-destination-offset" data-toc-modified-id="Get-destination-offset-7.10"><span class="toc-item-num">7.10&nbsp;&nbsp;</span>Get destination offset</a></span></li></ul></li><li><span><a href="#Autopilot-routines" data-toc-modified-id="Autopilot-routines-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Autopilot routines</a></span><ul class="toc-item"><li><span><a href="#Undock" data-toc-modified-id="Undock-8.1"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>Undock</a></span></li><li><span><a href="#Dock" data-toc-modified-id="Dock-8.2"><span class="toc-item-num">8.2&nbsp;&nbsp;</span>Dock</a></span></li><li><span><a href="#Align" data-toc-modified-id="Align-8.3"><span class="toc-item-num">8.3&nbsp;&nbsp;</span>Align</a></span></li><li><span><a href="#Jump" data-toc-modified-id="Jump-8.4"><span class="toc-item-num">8.4&nbsp;&nbsp;</span>Jump</a></span></li><li><span><a href="#Refuel" data-toc-modified-id="Refuel-8.5"><span class="toc-item-num">8.5&nbsp;&nbsp;</span>Refuel</a></span></li><li><span><a href="#Position" data-toc-modified-id="Position-8.6"><span class="toc-item-num">8.6&nbsp;&nbsp;</span>Position</a></span></li></ul></li><li><span><a href="#Autopilot-main" data-toc-modified-id="Autopilot-main-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Autopilot main</a></span><ul class="toc-item"><li><span><a href="#status-reference" data-toc-modified-id="status-reference-9.1"><span class="toc-item-num">9.1&nbsp;&nbsp;</span>status reference</a></span></li></ul></li></ul></div>

# ## References

# Useful docs / articles / etc
#   
#   1 - [A Python wrapper around AHK](https://pypi.org/project/ahk/)
# 
#   2 - [OpenCV on Wheels](https://pypi.org/project/opencv-python/)
# 
#   3 - [Autopilot for Elite Dangerous using OpenCV and thoughts on CV enabled bots in visual-to-keyboard loop](https://networkgeekstuff.com/projects/autopilot-for-elite-dangerous-using-opencv-and-thoughts-on-cv-enabled-bots-in-visual-to-keyboard-loop/)
#   
#   4 - [Using PyInstaller to Easily Distribute Python Applications](https://realpython.com/pyinstaller-python/)
#   
#   5 - [Direct Input to a Game - Python Plays GTA V](https://pythonprogramming.net/direct-input-game-python-plays-gta-v/)
#   
#   6 - [Cross-platform GUI automation for human beings](https://pyautogui.readthedocs.io/en/latest/index.html)

# ## Imports

# In[320]:


import sys
import datetime
from os import environ, listdir
from os.path import join, isfile, getctime, abspath
from json import loads
from math import degrees, atan
from time import sleep
from numpy import array, sum, where
from PIL import ImageGrab
from datetime import datetime
from xml.etree.ElementTree import parse
import cv2 # see reference 2
from src.directinput import * # see reference 5
from pyautogui import size# see reference 6


# In[321]:


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath(".")

    return join(base_path, relative_path)


# ## Constants

# In[322]:


PATH_LOG_FILES = None
PATH_KEYBINDINGS = None
KEY_MOD_DELAY = 0.200
KEY_DEFAULT_DELAY = 0.200
KEY_REPEAT_DELAY = 0.150
FUNCTION_DEFAULT_DELAY = 0.500
SCREEN_WIDTH, SCREEN_HEIGHT = size()


# ## Read ED logs

# ### Get latest log file

# In[323]:


def get_latest_log(path_logs=None):
    """Returns the full path of the latest (most recent) elite log file (journal) from specified path"""
    if not path_logs:
        path_logs = environ['USERPROFILE'] + "\Saved Games\Frontier Developments\Elite Dangerous"
    list_of_logs = [join(path_logs, f) for f in listdir(path_logs) if isfile(join(path_logs, f)) and f.startswith('Journal.')]
    if not list_of_logs:
        return None
    latest_log = max(list_of_logs, key=getctime)
    return latest_log


# In[324]:


# get_latest_log(PATH_LOG_FILES)


# ### Extract ship info from log

# In[325]:


def ship():
    """Returns a 'status' dict containing relevant game status information (state, fuel, ...)"""
    latest_log = get_latest_log(PATH_LOG_FILES)
    ship = {
        'time': (datetime.now() - datetime.fromtimestamp(getctime(latest_log))).seconds,
        'status': None,
        'location': None,
        'target': None,
        'fuel_capacity': None,
        'fuel_level': None,
        'fuel_percent': None,
        'is_scooping': False,
    }
    # Read log line by line and parse data
    with open(latest_log, encoding="utf-8") as f:
        for line in f:
            log = loads(line)
            
            # parse data
            try:
                # parse ship status
                log_event = log['event']
                
                if log_event == 'StartJump':
                    ship['status'] = str('starting_'+log['JumpType']).lower()
                    
                elif log_event == 'SupercruiseEntry' or log_event == 'FSDJump':
                    ship['status'] = 'in_supercruise'
                    
                elif log_event == 'SupercruiseExit' or log_event == 'DockingCancelled'                  or (log_event == 'Music' and ship['status'] == 'in_undocking')                  or (log_event == 'Location' and log['Docked'] == False):
                    ship['status'] = 'in_space'
                    
                elif log_event == 'undockinged':
                    ship['status'] = 'starting_undocking'
                    
                elif log_event == 'DockingRequested':
                    ship['status'] = 'starting_docking'
                    
                elif log_event == "Music" and log['MusicTrack'] == "DockingComputer":
                    if ship['status'] == 'starting_undocking':
                        ship['status'] = 'in_undocking'
                    elif ship['status'] == 'starting_docking':
                        ship['status'] = 'in_docking'
                
                elif log_event == 'Docked':
                    ship['status'] = 'in_station'
                    
                # parse fuel
                if 'FuelCapacity' in log and 'FuelLevel' in log:
                    ship['fuel_capacity'] = log['FuelCapacity']
                    ship['fuel_level'] = log['FuelLevel']
                    ship['fuel_percent'] = round((ship['fuel_level'] / ship['fuel_capacity'])*100)
                elif log_event == 'FuelScoop' and 'Total' in log:
                    ship['fuel_level'] = log['Total']
                    ship['fuel_percent'] = round((ship['fuel_level'] / ship['fuel_capacity'])*100)
                elif 'FuelLevel' in log:
                    ship['fuel_level'] = log['FuelLevel']
                    ship['fuel_percent'] = round((ship['fuel_level'] / ship['fuel_capacity'])*100)
                    
                # parse scoop
                if log_event == 'FuelScoop' and ship['time'] < 10 and ship['fuel_percent'] < 100:
                    ship['is_scooping'] = True
                else:
                    ship['is_scooping'] = False
                    
                # parse location
                if (log_event == 'Location' or log_event == 'FSDJump') and 'StarSystem' in log:
                    ship['location'] = log['StarSystem']
                    
                # parse target
                if log_event == 'FSDTarget':
                    if log['Name'] == ship['location']:
                        ship['target'] = None
                    else:
                        ship['target'] = log['Name']
                elif log_event == 'FSDJump':
                    if ship['location'] == ship['target']:
                        ship['target'] = None
                
                    
            # exceptions
            except Exception as e:
                print(e)
    return ship


# In[326]:


# ship()


# ## Control ED with direct input

# ### Get necessary keybinds

# In[327]:


def get_bindings(path_bindings=None):
    """Returns a dict struct with the direct input equivalent of the necessary elite keybindings"""
    direct_input_keys = {}
    keys_to_obtain = [
        'PitchUpButton',
        'PitchDownButton',
        'RollLeftButton',
        'RollRightButton',
        'YawLeftButton',
        'YawRightButton',
        'SetSpeedZero',
        'SetSpeed100',
        'UI_Back',
        'UIFocus',
        'UI_Up',
        'UI_Down',
        'UI_Left',
        'UI_Right',
        'UI_Select',
        'CycleNextPanel',
        'HeadLookReset',
        'HyperSuperCombination'
    ]
    convert_to_direct_keys = {
        'Key_LeftShift':'LShift',
        'Key_RightShift':'RShift',
        'Key_LeftAlt':'LAlt',
        'Key_RightAlt':'RAlt',
        'Key_LeftControl':'LControl',
        'Key_RightControl':'RControl'
    }
    if not path_bindings:
        path_bindings = environ['LOCALAPPDATA'] + "\Frontier Developments\Elite Dangerous\Options\Bindings"
    list_of_bindings = [join(path_bindings, f) for f in listdir(path_bindings) if isfile(join(path_bindings, f))]
    if not list_of_bindings:
        return None
    latest_bindings = max(list_of_bindings, key=getctime)
    bindings_tree = parse(latest_bindings)
    bindings_root = bindings_tree.getroot()
    for item in bindings_root:
        if item.tag in keys_to_obtain:
            binding = {'key': SCANCODE['DIK_'+str(item[0].attrib['Key'][4:]).upper()]}
            if len(item[0]) > 0:
                mod = item[0][0].attrib['Key']
                if mod in convert_to_direct_keys:
                    mod = convert_to_direct_keys[mod]
                else:
                    mod = mod[4:]
                binding['mod'] = SCANCODE['DIK_'+mod.upper()]
            direct_input_keys[item.tag] = binding
    if len(list(direct_input_keys.keys())) < 1:
        return None
    else:
        return direct_input_keys


# In[328]:


keys = get_bindings(PATH_KEYBINDINGS)
# keys


# ## Direct input function

# In[329]:


def send(key, hold=None, repeat=1, repeat_delay=None, state=None):
    global KEY_MOD_DELAY, KEY_DEFAULT_DELAY, KEY_REPEAT_DELAY
    
    for i in range(repeat):
        
        if state is None or state == 1:
            if 'mod' in key:
                PressKey(key['mod'])
                sleep(KEY_MOD_DELAY)

            PressKey(key['key'])

        if state is None:
            if hold:
                sleep(hold)
            else:
                sleep(KEY_DEFAULT_DELAY)

        if state is None or state == 0:
            ReleaseKey(key['key'])

            if 'mod' in key:
                sleep(KEY_MOD_DELAY)
                ReleaseKey(key['mod'])
        
        if repeat_delay:
            sleep(repeat_delay)
        else:
            sleep(KEY_REPEAT_DELAY)


# In[330]:


# sleep(3)
# send(keys['UIFocus'], state=1)


# ## OpenCV

# ### Get screen

# In[331]:


def get_screen(x_left, y_top, x_right, y_bot):
    screen = array(ImageGrab.grab(bbox=(x_left, y_top, x_right, y_bot)))
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen
    


# ### HSV slider tool

# In[332]:


def callback(x):
    pass

def hsv_slider():
    cv2.namedWindow('image')

    ilowH = 0
    ihighH = 179

    ilowS = 0
    ihighS = 255
    ilowV = 0
    ihighV = 255

    # create trackbars for color change
    cv2.createTrackbar('lowH','image',ilowH,179,callback)
    cv2.createTrackbar('highH','image',ihighH,179,callback)

    cv2.createTrackbar('lowS','image',ilowS,255,callback)
    cv2.createTrackbar('highS','image',ihighS,255,callback)

    cv2.createTrackbar('lowV','image',ilowV,255,callback)
    cv2.createTrackbar('highV','image',ihighV,255,callback)

    while(True):
        # grab the frame
        frame = get_screen((5/16)*SCREEN_WIDTH, (5/8)*SCREEN_HEIGHT,(2/4)*SCREEN_WIDTH, (15/16)*SCREEN_HEIGHT)

        # get trackbar positions
        ilowH = cv2.getTrackbarPos('lowH', 'image')
        ihighH = cv2.getTrackbarPos('highH', 'image')
        ilowS = cv2.getTrackbarPos('lowS', 'image')
        ihighS = cv2.getTrackbarPos('highS', 'image')
        ilowV = cv2.getTrackbarPos('lowV', 'image')
        ihighV = cv2.getTrackbarPos('highV', 'image')

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_hsv = array([ilowH, ilowS, ilowV])
        higher_hsv = array([ihighH, ihighS, ihighV])
        mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

        frame = cv2.bitwise_and(frame, frame, mask=mask)

        # show thresholded image
        cv2.imshow('image', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# In[333]:


# hsv_slider()


# ### Filter sun

# In[334]:


def filter_sun(image=None, testing=False):
    while True:
        if testing:
            hsv = get_screen((1/3)*SCREEN_WIDTH, (1/3)*SCREEN_HEIGHT,(2/3)*SCREEN_WIDTH, (2/3)*SCREEN_HEIGHT)
        else:
            hsv = image.copy()
        # converting from BGR to HSV color space
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
        # filter Elite UI orange
        filtered = cv2.inRange(hsv, array([0, 100, 240]), array([180, 255, 255]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered


# In[335]:


# filter_sun(testing=True)


# ### Filter orange

# In[336]:


def filter_orange(image=None, testing=False):
    while True:
        if testing:
            hsv = get_screen((1/3)*SCREEN_WIDTH, (1/3)*SCREEN_HEIGHT,(2/3)*SCREEN_WIDTH, (2/3)*SCREEN_HEIGHT)
        else:
            hsv = image.copy()
        # converting from BGR to HSV color space
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
        # filter Elite UI orange
        filtered = cv2.inRange(hsv, array([0, 130, 123]), array([25, 235, 220]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered


# In[337]:


# filter_orange(testing=True)


# ### Filter orange2

# In[338]:


def filter_orange2(image=None, testing=False):
    while True:
        if testing:
            hsv = get_screen((1/3)*SCREEN_WIDTH, (1/3)*SCREEN_HEIGHT,(2/3)*SCREEN_WIDTH, (2/3)*SCREEN_HEIGHT)
        else:
            hsv = image.copy()
        # converting from BGR to HSV color space
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
        # filter Elite UI orange
        filtered = cv2.inRange(hsv, array([15, 220, 220]), array([30, 255, 255]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered


# In[339]:


# filter_orange2(testing=True)


# ### Filter blue

# In[340]:


def filter_blue(image=None, testing=False):
    while True:
        if testing:
            hsv = get_screen((1/3)*SCREEN_WIDTH, (1/3)*SCREEN_HEIGHT,(2/3)*SCREEN_WIDTH, (2/3)*SCREEN_HEIGHT)
        else:
            hsv = image.copy()
        # converting from BGR to HSV color space
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
        # filter Elite UI orange
        filtered = cv2.inRange(hsv, array([80, 0, 180]), array([140, 100, 255]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered


# In[341]:


# filter_blue(testing=True)


# ### Get sun

# In[342]:


def sun_percent():
    screen = get_screen((1/3)*SCREEN_WIDTH, (1/3)*SCREEN_HEIGHT,(2/3)*SCREEN_WIDTH, (2/3)*SCREEN_HEIGHT)
    filtered = filter_sun(screen)
    total = (1/3)*SCREEN_WIDTH*(1/3)*SCREEN_HEIGHT
    white = sum(filtered == 255)
    black = sum(filtered != 255)
    result = white / black
    return result * 100


# In[343]:


# sleep(3)
# sun_percent()


# ### Get compass image

# In[344]:


def get_compass_image(testing=False):
    compass_template = cv2.imread(resource_path("templates/compass.png"), cv2.IMREAD_GRAYSCALE)
    compass_width, compass_height = compass_template.shape[::-1]
    compass_image = compass_template.copy()
    doubt = 10
    while True:
        screen = get_screen((5/16)*SCREEN_WIDTH, (5/8)*SCREEN_HEIGHT,(2/4)*SCREEN_WIDTH, (15/16)*SCREEN_HEIGHT)
        mask_orange = filter_orange(screen)
        match = cv2.matchTemplate(mask_orange, compass_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.3
        loc = where( match >= threshold)
        pt = (doubt, doubt)
        for point in zip(*loc[::-1]):
                pt = point
        compass_image = screen[pt[1]-doubt : pt[1]+compass_height+doubt, pt[0]-doubt : pt[0]+compass_width+doubt].copy()
        if testing:
            cv2.rectangle(screen, pt, (pt[0] + compass_width, pt[1] + compass_height), (0,0,255), 2)
            cv2.imshow('Compass Found', screen)
            cv2.imshow('Compass Mask', mask_orange)
            cv2.imshow('Compass', compass_image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return compass_image, compass_width+(2*doubt), compass_height+(2*doubt)


# In[345]:


# get_compass_image(testing=True)


# ### Get navpoint offset

# In[346]:


def get_navpoint_offset(testing=False):
    navpoint_template = cv2.imread(resource_path("templates/navpoint.png"), cv2.IMREAD_GRAYSCALE)
    navpoint_width, navpoint_height = navpoint_template.shape[::-1]
    pt = (0, 0)
    while True:
        compass_image, compass_width, compass_height = get_compass_image()
        mask_blue = filter_blue(compass_image)
        match = cv2.matchTemplate(mask_blue, navpoint_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.5
        loc = where( match >= threshold)
        for point in zip(*loc[::-1]):
                pt = point
        final_x = (pt[0] + ((1/2)*navpoint_width)) - ((1/2)*compass_width)
        final_y = ((1/2)*compass_height) - (pt[1] + ((1/2)*navpoint_height))
        if testing:
            cv2.rectangle(compass_image, pt, (pt[0] + navpoint_width, pt[1] + navpoint_height), (0,0,255), 2)
            cv2.imshow('Navpoint Found', compass_image)
            cv2.imshow('Navpoint Mask', mask_blue)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    if pt[0] == 0 and pt[1] == 0:
        return {'x':-1, 'y':100}
    else:
        return {'x':final_x, 'y':final_y}


# In[347]:


# get_navpoint_offset(testing=True)


# ### Get destination offset

# In[348]:


def get_destination_offset(testing=False):
    destination_template = cv2.imread(resource_path("templates/destination.png"), cv2.IMREAD_GRAYSCALE)
    destination_width, destination_height = destination_template.shape[::-1]
    pt = (0, 0)
    width = (1/3)*SCREEN_WIDTH
    height = (1/3)*SCREEN_HEIGHT
    while True:
        screen = get_screen((1/3)*SCREEN_WIDTH, (1/3)*SCREEN_HEIGHT,(2/3)*SCREEN_WIDTH, (2/3)*SCREEN_HEIGHT)
        mask_orange = filter_orange2(screen)
        match = cv2.matchTemplate(mask_orange, destination_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.2
        loc = where( match >= threshold)
        for point in zip(*loc[::-1]):
                pt = point
        final_x = (pt[0] + ((1/2)*destination_width)) - ((1/2)*width)
        final_y = ((1/2)*height) - (pt[1] + ((1/2)*destination_height))
        if testing:
            cv2.rectangle(screen, pt, (pt[0] + destination_width, pt[1] + destination_height), (0,0,255), 2)
            cv2.imshow('Destination Found', screen)
            cv2.imshow('Destination Mask', mask_orange)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    if pt[0] == 0 and pt[1] == 0:
        return None
    else:
        return {'x':final_x, 'y':final_y}


# In[349]:


# sleep(3)
# get_destination_offset(testing=True)


# ## Autopilot routines

# ### Undock

# In[350]:


def undock():
    if ship()['status'] != "in_station":
        raise Exception('undock error 1')
    send(keys['UI_Back'], repeat=10)
    send(keys['HeadLookReset'])
    send(keys['UI_Down'], hold=3)
    send(keys['UI_Select'])
    sleep(1)
    if not (ship()['status'] == "starting_undock" or ship()['status'] == "in_undock"):
        raise Exception("undock error 2")
    send(keys['HeadLookReset'])
    send(keys['SetSpeedZero'], repeat=2)
    wait = 120
    for i in range(wait):
        sleep(1)
        if i > wait - 1:
            raise Exception('undock error 3')
        if ship()['status'] == "in_space":
            break
    return True


# In[351]:


# sleep(3)
# undock()


# ### Dock

# In[352]:


def dock():
    if ship()['status'] != "in_space":
        raise Exception('dock error 1')
    tries = 3
    for i in range(tries):
        send(keys['UI_Back'], repeat=10)
        send(keys['HeadLookReset'])
        send(keys['UIFocus'], state=1)
        send(keys['UI_Left'])
        send(keys['UIFocus'], state=0)
        send(keys['CycleNextPanel'], repeat=2)
        send(keys['UI_Up'], hold=3)
        send(keys['UI_Right'])
        send(keys['UI_Select'])
        sleep(1)
        if ship()['status'] == "starting_dock" or ship()['status'] == "in_dock":
            break
        if i > tries-1:
            raise Exception("dock error 2")
    send(keys['UI_Back'])
    send(keys['HeadLookReset'])
    send(keys['SetSpeedZero'], repeat=2)
    wait = 120
    for i in range(wait):
        sleep(1)
        if i > wait-1:
            raise Exception('dock error 3')
        if ship()['status'] == "in_station":
            break
    send(keys['UI_Up'], hold=3)
    send(keys['UI_Down'])
    send(keys['UI_Select'])
    return True


# In[353]:


# sleep(3)
# dock()


# ### Align

# In[354]:


def x_angle(point=None):
    if not point:
        return None
    result = degrees(atan(point['y']/point['x']))
    if point['x'] > 0:
        return +90 - result
    else:
        return -90 - result


# In[355]:


def align():
    if not (ship()['status'] == 'in_supercruise' or ship()['status'] == 'in_space'):
        raise Exception('not ready to jump')
    
    send(keys['SetSpeed100'])
    
    while sun_percent() > 5:
        send(keys['PitchUpButton'], state=1)
    send(keys['PitchUpButton'], state=0)
    
    close = 3
    close_a = 8
    hold_pitch = 0.5
    hold_roll = 0.3
    off = get_navpoint_offset()
    ang = x_angle(off)
    while (off['x'] > close and ang > close_a) or           (off['x'] < -close and ang < -close_a) or           (off['y'] > close) or           (off['y'] < -close):
        
        if off['x'] > close and ang > close:
            send(keys['RollRightButton'], hold=hold_roll)
        if off['x'] < -close and ang < -close:
            send(keys['RollLeftButton'], hold=hold_roll)
        if off['y'] > close:
            send(keys['PitchUpButton'], hold=hold_pitch)
        if off['y'] < -close:
            send(keys['PitchDownButton'], hold=hold_pitch)
            
        if ship()['status'] == 'starting_hyperspace':
            return
        off = get_navpoint_offset()
        ang = x_angle(off)
        
    sleep(0.5)    
    close = 80
    hold_pitch = 0.2
    hold_yaw = 0.3
    off = get_destination_offset()
    if not off:
        return
    while (off['x'] > close) or           (off['x'] < -close) or           (off['y'] > close) or           (off['y'] < -close):
        
        if off['x'] > close and ang > close:
            send(keys['YawRightButton'], hold=hold_yaw)
        if off['x'] < -close and ang < -close:
            send(keys['YawLeftButton'], hold=hold_yaw)
        if off['y'] > close:
            send(keys['PitchUpButton'], hold=hold_pitch)
        if off['y'] < -close:
            send(keys['PitchDownButton'], hold=hold_pitch)
            
        if ship()['status'] == 'starting_hyperspace':
            return
        off = get_destination_offset()
        if not off:
            return


# In[356]:


# sleep(3)
# align()


# ### Jump

# In[357]:


def jump():
    tries = 3
    for i in range(tries):
        if not (ship()['status'] == 'in_supercruise' or ship()['status'] == 'in_space'):
            raise Exception('not ready to jump')
        send(keys['HyperSuperCombination'])
        sleep(16)
        if ship()['status'] != 'starting_hyperspace':
            send(keys['HyperSuperCombination'])
            align()
        else:
            while ship()['status'] != 'in_supercruise':
                sleep(1)
            send(keys['SetSpeedZero'])
            return True
    raise Exception("jump failure")    


# ### Refuel

# In[358]:


def refuel():
    if ship()['status'] != 'in_supercruise':
        raise Exception('not ready to refuel')
    if not ship()['fuel_percent'] < 20:
        return
    send(keys['SetSpeed100'])
#     while not ship()['is_scooping']:
#         sleep(1)
    sleep(4)
    send(keys['SetSpeedZero'], repeat=3)
    while not ship()['fuel_percent'] == 100:
        sleep(1)
    return True


# In[359]:


# sleep(3)
# refuel()


# ### Position

# In[360]:


def position():
    send(keys['PitchUpButton'], hold=5)
    send(keys['SetSpeed100'])
    while sun_percent() > 5:
        send(keys['PitchUpButton'], state=1)
    sleep(3)
    send(keys['PitchUpButton'], state=0)
    sleep(15)
    return True


# In[361]:


# sleep(3)
# position()


# ## Autopilot main

# ### status reference
# 
# 'in-station'
# 
# 'in-supercruise'
# 
# 'in-space'
# 
# 'starting-undocking'
# 
# 'in-undocking'
# 
# 'starting-docking'
# 
# 'in-docking'

# In[362]:


def autopilot():
#     if ship()['target']:
#         undock()
    while ship()['target']:
        if ship()['status'] == 'in_space' or ship()['status'] == 'in_supercruise':
            align()
            jump()
            refuel()
            position()
        send(keys['SetSpeedZero'])


# In[363]:


# sleep(3)
# autopilot()

