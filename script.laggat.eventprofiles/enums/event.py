class SimpleEnum(object):
    @classmethod
    def getName(cls, val):
        # generate only once as we WILL not change here!
        if not hasattr(cls, '__reversed'):
            cls.__reversed = {v: k for k, v in cls.__dict__.items()}
        return cls.__reversed[val]
    @classmethod
    def getByName(cls, val):
        if not cls.__dict__[val]:
            return None
        return cls.__dict__[val]

""" names of events we could register to """
class EVENTS(SimpleEnum):
    Player_onPlaybackStarted = 1
    Player_onPlayBackEnded = 2

