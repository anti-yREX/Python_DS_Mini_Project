import comm_s


#1 Join the master - Login
#2 Recieve the command
#3 Execute the command
#4 Return the Result to the Master
#5 Log out

#Required Function Definations:
#Decode Time Message from string to Tuple
def decode_time(msg):
    pos = [-1, -1, -1]
    for x in range(len(msg)):
        if msg[x] == '[':            
            pos[0] = x+1
            continue
        if msg[x] == ',':
            pos[1] = x
            continue
        if msg[x] == ']':
            pos[2] = x
    min = msg[pos[0]:pos[1]]
    sec = msg[(pos[1]+1):pos[2]]
    return (int(min) , int(sec))


#1 Join the master - Login
addr = comm_s.send_message_to_master()


#2 Recieve the command
msg = comm_s.listen_to_master(addr)
id = int(msg[0])
ex_tm = decode_time(msg)
print("Slave "+str(id)+" : "+str(ex_tm))


#3 Execute the command
#wait_for_time(ex_tm)
#execute on time
#


#4 Return the Result


#5 Log out