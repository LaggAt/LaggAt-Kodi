from xbmc import Monitor
from enums.event import EVENTS

class MonitorEvents(Monitor):
    def __init__(self, callback=None):
        self.__callback = callback
        super(MonitorEvents, self).__init__()