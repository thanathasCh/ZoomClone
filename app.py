import threading
import requests
import socket
import gui
from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer

local_ip_address = socket.gethostbyname(socket.gethostname())
server = StreamingServer(local_ip_address, 9999)
