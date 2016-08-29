# -*- coding: utf-8 -*-
import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import os

__datapath__ = xbmc.translatePath("special://userdata/addon_data/script.audioswitch/")
__addon__ = xbmcaddon.Addon(sys.argv[0])
localize = __addon__.getLocalizedString

#__datapath__ = __addon__.getAddonInfo('path').decode('utf-8')
__setupMUSIC__ = localize( 30100 )  #'Go to the Audio Settings and set the Audio Device for *MUSIC*.\nAfter Configuration play an AUDIO File!'
__setupVIDEO__ = localize( 30101 )  #'Go to the Audio Settings and set the Audio Device for *VIDEO*.\nAfter Configuration play a VIDEO File!'
__setupDONE__ = localize( 30102 ) #Configuration is now DONE!
__setupMUSICSave__ = localize( 30103 ) #Audio Device for *MUSIC* saved!
__setupVIDEOSave__ = localize( 30104 ) #Audio Device for *VIDEO* saved!
__setupSTART__ = localize( 30105 ) #Start Setup for the Automatic Audio Switch?
__setupABORTED__ = localize( 30106 ) #Setup Aborted!
__setupDONETitle__ = localize( 30107 ) #DONE
__setupSETUPitle__ = localize( 30108 ) #SETUP


def set_audio(fi, device):
    f = xbmcvfs.File(os.path.join(__datapath__,fi.decode('utf-8')), 'w')
    result = f.write(device)
    f.close()

def get_audio(fi):
    f = xbmcvfs.File(os.path.join(__datapath__,fi.decode('utf-8')))
    result = f.read()
    f.close()
    return str(result)

def set_audiodevice(dev,pt,ch,volume):
    if volume != "disabled":
        xbmc.executebuiltin("SetVolume(%s)" % volume)
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.audiodevice","value":"%s"},"id":1}' % dev)
    xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.passthrough","value":%s}, "id":1}' % pt)
    xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.channels","value":%s}, "id":1}' % ch)

def gui_device():
    guidev = __addon__.getSetting("gui_device")
    if guidev == "VIDEO":
        vid = get_audio("device video.cfg")
        ptv = __addon__.getSetting("device_video_pt")
        chv = dict_channels2[__addon__.getSetting("device_video_ch")]
        #vvol = __addon__.getSetting("video_volume")		#Changing back to GUI Sounds won't change volume anymore
        set_audiodevice(vid,ptv,chv,'disabled')
    if guidev == "MUSIC":
        aud = get_audio("device audio.cfg")
        pta = __addon__.getSetting("device_audio_pt")
        cha = dict_channels2[__addon__.getSetting("device_audio_ch")]
        #avol = __addon__.getSetting("audio_volume")		#Changing back to GUI Sounds won't change volume anymore
        set_audiodevice(aud,pta,cha,'disabled')

#---------------------------------------------------------------------------------------
def setUP_video():						# SET OR SETUP AUDIO DEVICE FOR !!! VIDEO !!! -----------------------------------------------------------------------
    global setup_ready
    global current_dev
    setup = __addon__.getSetting("setup")
    vid = get_audio("device video.cfg")
    aud = get_audio("device audio.cfg")
    ptv = __addon__.getSetting("device_video_pt")
    chv = dict_channels2[__addon__.getSetting("device_video_ch")]
    vvol = __addon__.getSetting("video_volume")

    if setup == "true":					# SETUP AUDIO DEVICE FOR VIDEO -----------------------------------------------------------------------
        vid = xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettingValue", "params":{"setting":"audiooutput.audiodevice"},"id":1}')
        vid = str(vid[43:-3].decode('utf-8'))
        print "-------------------------------------------- DEVICE FOR VIDEO: " + str(vid)
        ptv = xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.GetSettingValue", "params":{"setting":"audiooutput.passthrough"}, "id":1}')
        chv = xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.GetSettingValue", "params":{"setting":"audiooutput.channels"}, "id":1}')
        ptv = ptv[ptv.find("value")+7:-2]

        __addon__.setSetting("device_video_pt", ptv)
        if not "error" in chv:
		    chv = chv[chv.find("value")+7:-2]
		    __addon__.setSetting("device_video_ch", dict_channels[chv])
        set_audio("device video.cfg", vid) 
        dialog = xbmcgui.Dialog()
        ok = dialog.ok(__setupDONETitle__, __setupVIDEOSave__)
        if aud == "":
            ok = dialog.ok(__setupSETUPitle__, __setupMUSIC__)
            xbmc.executebuiltin("PlayerControl(Stop)")
        else:
            __addon__.setSetting("setup", "false")
            ok = dialog.ok(__setupDONETitle__, __setupDONE__)
            xbmc.executebuiltin("PlayerControl(Stop)")
            setup_ready = False
    else:						# SET AUDIO DEVICE FOR VIDEO -----------------------------------------------------------------------
        #check if last playing audio device differs from new one -> if yes, change volume, otherwise don't
        if current_dev != vid:
            set_audiodevice(vid,ptv,chv,vvol)
            current_dev = vid
        else:
            set_audiodevice(vid,ptv,chv,'disabled')			#Need to set it tho, because GUI Sounds can use a different Device

#---------------------------------------------------------------------------------------
def setUP_audio():						# SET OR SETUP AUDIO DEVICE FOR !!! MUSIC !!! -----------------------------------------------------------------------
    global setup_ready
    global current_dev
    setup = __addon__.getSetting("setup")
    vid = get_audio("device video.cfg")
    aud = get_audio("device audio.cfg")
    pta = __addon__.getSetting("device_audio_pt")
    cha = dict_channels2[__addon__.getSetting("device_audio_ch")]
    avol = __addon__.getSetting("audio_volume")

    if setup == "true":					# SETUP AUDIO DEVICE FOR MUSIC -----------------------------------------------------------------------
        aud = xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettingValue", "params":{"setting":"audiooutput.audiodevice"},"id":1}')
        aud = str(aud[43:-3].decode('utf-8'))
        print "--------------------------------------------  DEVICE FOR AUDIO: " + str(aud)
        pta = xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.GetSettingValue", "params":{"setting":"audiooutput.passthrough"}, "id":1}')
        cha = xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.GetSettingValue", "params":{"setting":"audiooutput.channels"}, "id":1}')
        pta = pta[pta.find("value")+7:-2]

        __addon__.setSetting("device_audio_pt", pta)
        if not "error" in cha:
		    cha = cha[cha.find("value")+7:-2]
		    __addon__.setSetting("device_audio_ch", dict_channels[cha])
        set_audio("device audio.cfg", aud)
        dialog = xbmcgui.Dialog()
        ok = dialog.ok(__setupDONETitle__, __setupMUSICSave__)
        if vid == "":
            ok = dialog.ok(__setupSETUPitle__, __setupVIDEO__)
            xbmc.executebuiltin("PlayerControl(Stop)")
        else:
            __addon__.setSetting("setup", "false")
            ok = dialog.ok(__setupDONETitle__, __setupDONE__)
            xbmc.executebuiltin("PlayerControl(Stop)")
            setup_ready = False
    else:						# SET AUDIO DEVICE FOR MUSIC -----------------------------------------------------------------------
        #check if last playing audio device differs from new one -> if yes, change volume, otherwise don't
        if current_dev != aud:
            set_audiodevice(aud,pta,cha,avol)
            current_dev = aud
        else:
            set_audiodevice(aud,pta,cha,'disabled')			#Need to set it tho, because GUI Sounds can use a different Device

#---------------------------------------------------------------------------------------

class XBMCMonitor( xbmc.Monitor ):
    def __init__( self, *args ):
        pass

    def onSettingsChanged( self ):
        global setup_ready
        global swap
        swap = __addon__.getSetting("swap")
		
        setup = __addon__.getSetting("setup")
        if setup == "true" and setup_ready == False:
            dialog = xbmcgui.Dialog()
            if dialog.yesno(__setupSETUPitle__,__setupSTART__):
                ok = dialog.ok(__setupSETUPitle__, __setupMUSIC__)
                set_audio("device audio.cfg", "")
                set_audio("device video.cfg", "")
                __addon__.setSetting("swap", "false")
                setup_ready = True
            else:
                ok = dialog.ok(__setupSETUPitle__, __setupABORTED__)
                __addon__.setSetting("setup", "false")
            
#---------------------------------------------------------------------------------------

class XBMCPlayer( xbmc.Player ):

    def __init__( self, *args ):
        pass

    def onPlayBackStarted( self ):				# PLAYBACK STARTS
        print "PLAYBACK EVENT INVOKED"

        if (xbmc.Player().isPlayingVideo()):
            print "VIDEO IS PLAYING"
            if swap == "false":				
                setUP_video()
            else:
                setUP_audio()
    
        if (xbmc.Player().isPlayingAudio()):
      	    print "AUDIO IS PLAYING"
            if swap == "false":				
                setUP_audio()
            else:
                setUP_video()
			 
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        gui_device()
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        gui_device()


player = XBMCPlayer()
monitor = XBMCMonitor()
setup_ready = False
current_dev = ''
swap = __addon__.getSetting("swap")

dict_channels = {'1': '2.0', '2': '2.1', '3': '3.0', '4': '3.1', '5': '4.0', '6': '4.1', '7': '5.0', '8': '5.1', '9': '7.0', '10': '7.1'}
dict_channels2 = {'2.0': '1', '2.1': '2', '3.0': '3', '3.1': '4', '4.0': '5', '4.1': '6', '5.0': '7', '5.1': '8', '7.0': '9', '7.1': '10'}

while not monitor.abortRequested():
    if monitor.waitForAbort(10):
        break
