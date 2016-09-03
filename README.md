# LaggAt-Kodi - Addons and scripts for Kodi

I'll provide some scripts & plugins for kodi. I want to switch TV to on and standby using CEC/Scripts, switch video and audio settings based on events like 'playing music', 'playing video', the remote control used, ...

## Install:

[Please install the Repository ZIP from here.](https://github.com/LaggAt/LaggAt-Kodi/blob/master/_repo/repository.laggat/repository.laggat-0.1.1.zip?raw=true)

This is how you do it in kodi: 

1. Download ZIP on your Kodi machine
2. Go to Settings - file manager - browse the ZIP and install
3. You 'll find all available addons in Settings - Addons - Install from repository - Repository LaggAt

## Addons available:

* Excellent 'Automatic Audio Switcher' from Marv. I currently use it for one of my Kodi installations, and I want to extend it to my needs. It's easily installable via the repository above. Original source is [this thread on the Kodi forum](http://forum.kodi.tv/showthread.php?tid=201896&pid=1771231#pid1771231).

### Next Script/Addon I work on:

* Configurable Switch (even the name is WIP): this plugin will handle events from different sources like Kodi, the time, other scripts, ... Based on a ruleset it will be able to signal other plugins and scripts to do something. In easy words, it could handle requests like: when playing video --> turn the TV on. when playing audio --> switch to a bluetooth audio device, switch TV off. but when playing audio, but using a IR-Remote, turn the TV on so that the user can see what he selects. (the actions itself will be carried out by plugins registering to events in Configurable Switch)

Feel free to fork my work here, if you are a coder and want to help. Also feel free to file issues if you want features or find bugs.
