# Elite Dangerous: AutoPilot
Elite Dangerous computer vision and ahk based autopilot

Program uses AHK to control inputs in Elite Dangerous and Python scripts using OpenCV
to read information of the game screen and auto-navigate the ship through a set Route.



USAGE:

CONFIGURATION:
1. Download and extract zip.
2. Inside the "Data" folder extract "GetNavPointOffset.zip"
3. Open the "AutoPilot.ahk" and configure controls settings in section 1. (Optionally configure other settings)
4. Run the script and enter game.
5. Press PgUp key to initiate configuration wizard.
6. Optionally, plot route to nearby star, manually aim ship at the star and press F10 to check offset (should be close to 0,0)

AUTOPILOT:
1. Plot route in galaxy map OR press Insert key and type in destination.
2. Press Home key to initiate autopilot
3. Press End key at any time to abort and shutdown autopilot.

OTHER:
1. If you are changing ship and wish yo keep your settings just save the generated settings.txt file with a different name and replace as necessary

WARNING:
This NOT to be used unsupervised. Do so at your own and your own ship's risk!
