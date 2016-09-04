import xbmc
from enums.event import EVENTS

class Events(object):
    def __init__(self):
        ### All eventsource consolidated here
        self.__events_callbacks = {}

        # event sources (es)
        # later just load these really used in registries
        from eventsource.monitor import MonitorEvents # this is needed anyway for main loop
        self.esMonitor = MonitorEvents(callback=self.__incoming_event)
        from eventsource.player import PlayerEvents
        self.esPlayer = PlayerEvents(callback=self.__incoming_event)
        self.main()

    def main(self):
        xbmc.log("script.laggat.eventprofiles started & ready", level=xbmc.LOGDEBUG)
        while not self.esMonitor.abortRequested():
            if self.esMonitor.waitForAbort(5):
                return True
        xbmc.log("script.laggat.eventprofiles exited", level=xbmc.LOGDEBUG)


    def __incoming_event(self, event, e={}):
        evname = EVENTS.getName(event)
        print("Event %s fired" % (evname,))
        xbmc.log("Event %s fired" % (evname,),level=xbmc.LOGDEBUG)
        if self.__events_callbacks.has_key(event):
            for callback in self.__events_callbacks[event]:
                callback(e)

    """ callbacks should have the signature callback(e): where e is a dict containing event details. """
    def register(self, event, callback):
        if not callable(callback):
            xbmc.log("need to register callable(e), event: %s" % (event,), level=xbmc.LOGERROR)
            return
        evname = EVENTS.getName(event)
        if not evname:
            xbmc.log("event ID is unknown: %s" % (event,), level=xbmc.LOGERROR)
        else:
            xbmc.log("registered %s to event %s" % (callback.__name__, evname))

        if self.__events_callbacks.has_key(event):
            self.__events_callbacks[event] += [callback, ]