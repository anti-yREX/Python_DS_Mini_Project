import socket
def send_message_to_master(addr):
    s = socket.socket()
    s.connect(addr)
    data = s.recv(1024).decode('utf8')
    print(data)
    addr = s.getsockname()
    s.close()
    return addr

def listen_to_master(addrs):
    s = socket.socket()
    s.bind((addrs))
    print("Socket is binded to ",addrs[1])
    s.listen(5)
    print("Ther socket  is listening...")
    c, addr = s.accept()
    print("Connected to : ",addr)
    data = c.recv(1024).decode('utf8')
    c.close()
    s.close()
    return data

def send_result_to_master(msg,addr):
    s = socket.socket()
    s.connect((addr))
    s.send(msg.encode())
    s.close()
    return