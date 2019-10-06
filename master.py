import comm_m
from time import  gmtime
import threading

#1 Listen to all the Joining Slaves
#2 Log Slaves
#3 Divide the Work for the slaves
#4 Command the Slaves
#5 Evalute the result
#6 Log the slaves out

#Required Function Definations:
#Add two time values in Mins and Secs
def add_time(t1,t2):
     t3 = [0,0]
     t3[1] = ( t1[1] + t2[1] ) % 60
     t3[0] = ( t1[0] + t2[0] ) + ((t1[1] + t2[1])//60)
     return t3

flags = [True,True]
def sync_time():
    port = 8080
    n = 0
    while flags[0]==True:
        addr=comm_m.listen_to_slave(port+n)
        n = (n+1) % 5
        msg=gmtime()
        msg=[msg[4],msg[5]]
        print("Sending Time: "+ str(msg) +" to "+str(addr))
        comm_m.send_message_to_slave(str(msg),addr)
    return


#1 Listen to all the Joining Slaves
log = []
bool  = True
N = n = 3

while bool==True:
    log.append(comm_m.listen_to_slave(8088))
    n -= 1
    if n == 0:
        bool = False


#2 Log Slaves
print(log)


#3  Divide the Work for the Slaves
msg = []
c_t = gmtime()
c_tm = [c_t[4], c_t[5]]
print(c_tm)
x=11
ex_tm = [0, 5]
ex_tm = add_time(c_tm,ex_tm)
msg.append(ex_tm)
for i in range(1,N):
    ex_tm = add_time(ex_tm,[0,x])
    msg.append(ex_tm)
ex_tm = add_time(ex_tm,[0,x])
msg.append(ex_tm)
print(msg)
ex_tm = msg[len(msg)-1]
print("Master : "+str(ex_tm))


#4  Command the Slaves
i=0
for x in log:
    print("Replying "+str(x))
    comm_m.send_message_to_slave(str(i)+str(msg[i]), x)
    i += 1

#4 Sub Step 1: Syncronize Clocks
th1 = threading.Thread(target=sync_time)
th1.start()

#4 Sub Step 2: Executing Master's Job


#5  Evaluate the Result

th1.join()

#6 Log Slaves Out
log = []