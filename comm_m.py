import socket
def send_message_to_slave(msg, addr):
    s = socket.socket()
    s.connect((addr))
    print("Sending msg...")
    s.send(msg.encode())
    s.close()
    return

def listen_to_slave():
    s = socket.socket()
    port = 8088
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
