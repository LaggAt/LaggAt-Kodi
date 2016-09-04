from events import Events
import xbmc

import pydevd;
pydevd.settrace('192.168.144.144', port=5678, stdoutToServer=True, stderrToServer=True, suspend=False)

if __name__ == '__main__':
    try:
        exit = Events()
    except Exception as e:
        xbmc.log(e.message, level=xbmc.LOGERROR)

    #exiting: cleanup
    del Events