# Elite Dangerous: AutoPilot v2
Elite Dangerous computer vision based autopilot version 2

Program uses openCV and other tools in python to navigate automatically in Elite Dangerous.

Look [here for the autopilot alpha version release](https://github.com/skai2/EDAutopilot/releases).

# Warning:
The .exe file avalable on the release page is broken on many systems.\
Feel free to try it however if you get a popup saying `Failed to execute` then you will need to run from the source code untill the restructure is finished and a new .exe is created.

## Usage:
The program will create an icon on the taskbar.

  1. Setup a route in the galaxy map as you would normally, then:
  
  - Optionally right click the taskbar icon to set which fire group (primary or secondary) you have configured your discovery scanner to, to enable auto-scanner (remember you must have a *keyboard*, not mouse, binding as well)

  2. Press **Home** key to start autopilot.

  3. Press **End** key to abort autopilot.  

## Necessary Setup:
In game, you must have configured keyboard keys for all of the following. You may configure them in either
the left or the right slot, and this program will automatically fetch your most recent changes.
  * In 'Mouse Control':
    * Reset Mouse
  * In 'Flight Rotation':
    * Yaw Left
    * Yaw Right
    * Roll Left
    * Roll Right
    * Pitch Up
    * Pitch Down
  * In 'Flight Throttle':
    * Set Speed To 0%
    * Set Speed To 100%
  * In 'Flight Miscellaneous'
    * Toggle Frameshift Drive
  * In 'Mode Switches':
    * UI Focus
  * In 'Interface Mode':
    * UI Panel Up
    * UI Panel Down
    * UI Panel Left
    * UI Panel Right
    * UI Panel Select
    * UI Back
    * Next Panel Tab
  * In 'Headlook Mode':
    * Reset Headlook

## Optimal Game Settings:
1. Desktop & Game resolution:   1080p Borderless 
2. Ship UI color:               Orange (default colour)
3. Ship UI brightness:          Maximum

## General Guidelines

I recommend setting your route finder to use only scoopable stars. For full functionality, "Advanced Autodocking" module must be outfitted on ship. Definitely do not leave this running unsupervised unless you don't mind paying rebuy.

##
Or if you'd like to set it up and run the script directly...

## Setup:
_Requires **python 3** and **git**_
1. Clone this repository
```sh
> git clone https://github.com/skai2/EDAutopilot.git
```
2. Install requirements
```sh
> cd EDAutoPilot
> pip install -r requirements.txt
```
3. Run script
```sh
> python autopilot.py
OR you may have to run
> python3 autopilot.py
if you have both python 2 and 3 installed.
```

If you encounter any issues during pip install, try running:
> python -m pip install -r requirements.txt
instead of > pip install -r requirements.txt

## WARNING:

ALPHA VERSION IN DEVELOPMENT. 

Absolutely DO NOT LEAVE UNSUPERVISED. 

Use at YOUR OWN RISK.

## CONTACT:

# Email

skai2mail@gmail.com

# Discord

https://discord.gg/HCgkfSc
