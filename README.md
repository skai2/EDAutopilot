# Elite Dangerous: AutoPilot
Elite Dangerous computer vision and ahk based autopilot

Program uses AHK to control inputs in Elite Dangerous and Python scripts using OpenCV
to read information of the game screen and auto-navigate the ship through a set Route.



USAGE:

CONFIGURATION:
1. Download and extract zip.
2. Open the "AutoPilot.ahk" and configure controls settings in section 1. (Optionally configure other settings, but keep in mind that section 2 can be configured via step 4 below)
3. Run the script and enter game.
4. Press PgUp key to initiate configuration wizard.
5. Optionally, plot route to nearby star, manually aim ship at the star and press F10 to check offset (should be close to 0,0)
6. Optionally, point ship towards a star(F/G/K/M [Red/Yellow-ish planets]) at navpoint distance (The distance right after you FSD jump into a system), then press F9 to initiate a failsafe check to minimize your chance of accidentally flying into a star. 

AUTOPILOT:
1. Plot route in galaxy map OR press Insert key and type in destination.
2. Press Home key to initiate autopilot
3. Press End key at any time to abort and shutdown autopilot.

OTHER:
1. If you are changing ship and wish to keep your settings just save the generated settings.txt file with a different name and replace as necessary

WARNING:

This NOT to be used unsupervised. Do so at your own and your own ship's risk!

CONTACT:

skai2mail@gmail.com

ADD. FEATURES/MODIFIED BY:

eric@enumc.com
