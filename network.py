import socket

local_ip_address = socket.gethostbyname(socket.gethostname())
target_ip = None
steaming_port = 9999
receiving_port = 8888
target_port = 7777
audio_port = 6666