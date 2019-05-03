# Elite Dangerous: AutoPilot v2
Elite Dangerous computer vision based autopilot version 2

Program uses openCV and other tools in python to navigate automatically in Elite Dangerous.

Look [here](https://github.com/skai2/EDAutopilot/releases) for the alpha release.

## Usage:
The program will create an icon on the taskbar.

Press **Home** key to start autopilot.

Press **End** key to abort autopilot.

## Necessary Setup:
You must have configured primary keyboard keys for all of the following:
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
1. Game resolution:      1080p Borderless
2. Ship UI color:        Orange (default colour)
3. Ship UI brightness:   Maximum

## General Guidelines

I recommend setting your route finder to use only scoopable stars, Additionally, for full functionality, "Advanced Autodocking" module must be outfitted on ship. Definitely do not leave this running unsupervised unless you don't mind paying rebuy.

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
```

## WARNING:

ALPHA VERSION IN DEVELOPMENT. 

Absolutely DO NOT LEAVE UNSUPERVISED. 

Use at YOUR OWN RISK.

## CONTACT:

skai2mail@gmail.com
