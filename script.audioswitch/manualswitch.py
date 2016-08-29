import xbmc
import xbmcaddon
import xbmcvfs
import os

__datapath__ = xbmc.translatePath("special://userdata/addon_data/script.audioswitch/")
__addon__ = xbmcaddon.Addon("script.audioswitch")

#---------------------------------------------------------------------------------------
def get_audio(fi):
      f = xbmcvfs.File(os.path.join(__datapath__,fi.decode('utf-8')))
      result = f.read()
      f.close()
      return str(result)
#---------------------------------------------------------------------------------------
def set_audiodevice(dev,pt,ch,volume):
    if volume != "disabled":
       xbmc.executebuiltin("SetVolume(%s)" % volume)
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.audiodevice","value":"%s"},"id":1}' % dev)
    xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.passthrough","value":%s}, "id":1}' % pt)
    xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.channels","value":%s}, "id":1}' % ch)
#---------------------------------------------------------------------------------------

dict_channels = {'1': '2.0', '2': '2.1', '3': '3.0', '4': '3.1', '5': '4.0', '6': '4.1', '7': '5.0', '8': '5.1', '9': '7.0', '10': '7.1'}
dict_channels2 = {'2.0': '1', '2.1': '2', '3.0': '3', '3.1': '4', '4.0': '5', '4.1': '6', '5.0': '7', '5.1': '8', '7.0': '9', '7.1': '10'}
dict_truefalse = {'true': 'false', 'false': 'true'}

vid = get_audio("device video.cfg")
ptv = __addon__.getSetting("device_video_pt")
chv = dict_channels2[__addon__.getSetting("device_video_ch")]
vvol = __addon__.getSetting("video_volume")

aud = get_audio("device audio.cfg")
pta = __addon__.getSetting("device_audio_pt")
cha = dict_channels2[__addon__.getSetting("device_audio_ch")]
avol = __addon__.getSetting("audio_volume")

swap = dict_truefalse[__addon__.getSetting("swap")]
__addon__.setSetting("swap", swap)

if xbmc.Player().isPlaying():
       if (xbmc.Player().isPlayingAudio()):
            if swap == "true":
                set_audiodevice(vid,ptv,chv,vvol)
                xbmc.executebuiltin("Notification(AUDIO DEVICE,Audio output changed to VIDEO)")
            else:
                set_audiodevice(aud,pta,cha,avol)
                xbmc.executebuiltin("Notification(AUDIO DEVICE,Audio output changed to MUSIC)")
       
       if (xbmc.Player().isPlayingVideo()):
            if swap == "true":
                set_audiodevice(aud,pta,cha,avol)
                xbmc.executebuiltin("Notification(AUDIO DEVICE,Audio output changed to MUSIC)")
            else:
                set_audiodevice(vid,ptv,chv,vvol)
                xbmc.executebuiltin("Notification(AUDIO DEVICE,Audio output changed to VIDEO)")

else:
       if swap == "true":
               xbmc.executebuiltin("Notification(AUDIO DEVICE,Changing Audio output to *SWAP*)")
       else:
               xbmc.executebuiltin("Notification(AUDIO DEVICE,Changing Audio output to *NORMAL*)")

