import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "127.0.0.1"
port = 12345

s.connect((ip, port))
print("Connected to localhost.")
HTTPMessage = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"
data = str.encode(HTTPMessage)

s.sendall(data)

while True:
    
    dt = s.recv(1024)
    print(dt)
    
    if(dt == b""):
        print("Connection closed.")
        break
    
s.close()
