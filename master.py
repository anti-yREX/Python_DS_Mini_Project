import comm_m
from time import gmtime
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
def sync_time(port):
    while flags[0]==True:
        try:
            addr=comm_m.listen_to_slave(port)
        except:
            print("No Slaves available")
            continue
        msg=gmtime()
        msg=[msg[4],msg[5]]
        print("Sending Time: "+ str(msg) +" to "+str(addr))
        comm_m.send_message_to_slave(str(msg),addr)
        
    print("Time Sync at "+str(port)+" ended.")
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
x=5
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
th =  []
for i  in range(0,5):
    port = 8080+i
    t = threading.Thread(target=sync_time,args=[port])
    th.append(t)
    th[len(th)-1].start()

#5  Evaluate the Result
bool = True
n=N
while bool==True:
    msg = comm_m.recieve_result_from_slave(('127.0.0.1',8088))
    print(msg)
    n -= 1
    if n == 0:
        flags[0]=False
        bool = False
print(flags)
for i in th:
    i.join()


#6 Log Slaves Out
log = []