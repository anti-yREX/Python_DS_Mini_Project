import comm_s
from time import gmtime
import scrn_s

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

#Comapre Time  Values
def check_time(t1,t2):
    t1 = (t1[0] * 60) + t1[1]
    t2 = (t2[0] * 60) + t2[1]
    if(t1 > t2):return -1
    if(t1 == t2):return 0
    if(t1 < t2):return 1

#Wait for the Execution Time
def wait_for_time(ex_tm):
    bool = True
    port = 8080
    n=0
    while bool==True:
        try:
            print("Trying Port "+str(port+n))
            addr = comm_s.send_message_to_master(port+n)
        except:
            print("Port "+ str(port+n) +" is Busy.")
            n = (n+1) % 5
            continue
        msg = comm_s.listen_to_master(addr)
        tm = decode_time(msg)
        print("Checking "+ str(tm) +" with "+str(ex_tm))
        if (check_time(ex_tm,tm)==0 or check_time(ex_tm,tm)==1):
            bool = False

#1 Join the master - Login
addrs = ('192.168.43.196',8088)
addr = comm_s.send_message_to_master(addrs)

#2 Recieve the command
msg = comm_s.listen_to_master(addr)
id = int(msg[0])
win = scrn_s.initiate(id)
ex_tm = decode_time(msg)
print("Slave "+str(id)+" : "+str(ex_tm))


#3 Execute the command
wait_for_time(ex_tm)
strt_tm = gmtime()
strt_tm = [strt_tm[4],strt_tm[5]]
scrn_s.animate(win)
end_tm = gmtime()
end_tm = [end_tm[4], end_tm[5]]


#4 Return the Result
comm_s.send_result_to_master(str(id)+" "+str(strt_tm)+" "+str(end_tm),('127.0.0.1',8088))
print(str(strt_tm)+" "+str(end_tm))

#5 Log out