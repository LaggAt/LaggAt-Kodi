# script.audioswitch

## What is it?

It's a Service Addon which can setup DIFFERENT Audio Devices, one for Videos and one for Music WITHIN XBMC/KODI without fiddling around with logfiles or python code. When you play a Video- or Audiofile, it will switch to the pre-defined Audio Output automatically.

## How to setup?

1. Download and install the addon from here: [original download link](https://www.dropbox.com/s/v1gvutur8l5hvpo/script.audioswitch.0.2.3.zip?dl=0)
2. Go to the Service Addon Settings and enable "Run Audio Device Setup".
3. Go to the XBMC/KODI Audio Output Settings and set your Audio Device for MUSIC / AUDIO
4. Play an Audiofile (the Addon will save the Device plus Passthrough and Channels)
5. Do the same Step 3 and 4 for VIDEOS
6. Configuration is now done! From now on the Audio Device will switch automatically when playing a Video or Audio File.
7. (If you want you can go to the Addon Settings and define the GUI Audio Device as well.)
8. (You now even can set different volume levels for each Audio Device)

## Manual switch:

Additionally you can bind a key to XBMC.RunScript(special://home/addons/script.audioswitch/manualswitch.py) to toggle the Audio Devices manually.
if you deactivate the Service Addon, you still can use the manual switch.

I've tested it on Windows and Openelec!
Feedback is appreciated. thanks!

## CREDITS

The script was created by marv_el, on the [Kodi forum](http://forum.kodi.tv/showthread.php?tid=201896&pid=1771231#pid1771231) and released under the terms of GPL v2. Thanks. 
