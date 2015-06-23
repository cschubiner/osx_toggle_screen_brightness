# osx_toggle_screen_brightness
Turns on/off Mac's screen when run

Pair this script with something like Keyboard Maestro so you can turn the screen on and off with a hotkey (I recommend control+`).

### Keyboard Maestro pairing instructions
Use the control+` hotkey to activate your script.

Your script should be composed of just the `execute shell script` action. Point the action at `run_toggler.sh`

## Installation
This program requires [screenbrightness](https://github.com/jmstacey/screenbrightness) to be installed.

    brew install screenbrightness
