from xbmc import Player
from enums.event import EVENTS

class PlayerEvents(Player):
    def __init__(self, callback=None):
        self.__callback = callback
        super(PlayerEvents, self).__init__()

    def onPlayBackStarted(self):
        self.__callback(EVENTS.Player_onPlaybackStarted)
        super(PlayerEvents, self).onPlayBackStarted()

    def onPlayBackEnded(self):
        self.__callback(EVENTS.Player_onPlayBackEnded)
        super(PlayerEvents, self).onPlayBackEnded()
