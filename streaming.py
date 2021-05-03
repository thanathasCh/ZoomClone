import network
import threading
from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer

server = StreamingServer(network.local_ip_address, network.steaming_port)
receiver = AudioReceiver(network.local_ip_address, network.receiving_port)


def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()


def start_camera_steam():
    camera_client = CameraClient(network.target_ip, network.target_port)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()


def start_screen_sharing():
    screen_client = ScreenShareClient(network.target_ip, network.target_port)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()


def start_audio_stream():
    audio_sender = AudioSender(network.target_ip, network.audio_port)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

