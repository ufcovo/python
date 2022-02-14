import socket

localIP = "127.0.0.1"
localPort = 200001
bufferSize = 1024

msgFromServer = "Hello UDP Client."
bytesToSend = str.encode(msgFromServer)

UDPSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

UDPSocket.bind((localIP,localPort))

print("UDP server up and listening.")
while