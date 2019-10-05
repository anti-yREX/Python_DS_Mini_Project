import socket
def send_message_to_master():
    s = socket.socket()
    port= 8088
    s.connect(('127.0.0.1' , port))
    data = s.recv(1024).decode('utf8')
    print(data)
    addr = s.getsockname()
    s.close()
    return addr[1]

def listen_to_master(port):
    s = socket.socket()
    s.bind(('',port))
    print("Socket is binded to ",port)
    s.listen(5)
    print("Ther socket  is listening...")
    c, addr = s.accept()
    print("Connected to : ",addr)
    data = c.recv(1024).decode('utf8')
    print(data)
    c.close()
    s.close()
    return
 