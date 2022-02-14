import socket

ip = "127.0.0.1"
port = 12345


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server socket created.")
    
    s.bind((ip, port))
    print("Server socket bound with ip {} port {} ".format(ip, port))

    s.listen ()
    print("The socket is listening the connection.")
    
except socket.error as msg:
    print("Error: ", msg)
    
count = 0
while True:
    c, addr = s.accept()
    count = count + 1
    print("Accepted {} connections so far." .format(count))
    
    while True:
        
        data = s.recv(1024)
        print(data)
        
        if (data != b""):
            msg1 = "Hi Client. Read everything what we sent."
            msg1Bytes = str.encode(msg1)
            
            msg2 = "Now I will close your connection"
            msg2Bytes = str.encode(msg2)
            
            c.send (msg1Bytes)
            c.send (msg2Bytes)
            break
print("Connection closed.")
s.close()
