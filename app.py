import gui
import streaming

gui.init(streaming.start_listening,
         streaming.start_camera_steam,
         streaming.start_screen_sharing,
         streaming.start_audio_stream)