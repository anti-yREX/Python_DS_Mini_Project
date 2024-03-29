import socket
def send_message_to_slave(msg, addr):
    s = socket.socket()
    s.connect((addr))
    print("Sending msg...")
    s.send(msg.encode())
    s.close()
    return

def listen_to_slave(port):
    s = socket.socket()
    s.settimeout(15)
    s.bind(('', port))
    print("Socketis binded to ",port)
    s.listen(5)
    print("Ther socket  is listening...")
    c, addr = s.accept()
    print("Connected to : ",addr)
    c.send('Hello'.encode())
    c.close()
    s.close()
    return addr

def recieve_result_from_slave(addr):
    s = socket.socket()
    s.bind((addr))
    s.listen(5)
    c, addr = s.accept()
    msg = c.recv(1024).decode('utf8')
    c.close()
    s.close()
    return msg,addr
