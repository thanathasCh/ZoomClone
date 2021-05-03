import network
import threading
from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer

server = StreamingServer(network.local_ip_address, network.steaming_port)
receiver = AudioReceiver(network.local_ip_address, network.receiving_port)


def startListening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
