import comm_m
from time import  gmtime
#1 Listen to all the Joining Slaves
#2 Log Slaves
#3 Divide the Work for the slaves
#4 Command the Slaves
#5 Evalute the result
#6 Log the slaves out


#1 Listen to all the Joining Slaves
log = []
bool  = True
n = 3
while bool==True:
    log.append(comm_m.listen_to_slave())
    n -= 1
    if n == 0:
        bool = False
#2 Log Slaves
print(log)

#3  Divide the Work for the Slaves
c_tm = gmtime()
c_tm = (tm[4],tm[5])
print(tm)

#4  Command the Slaves
for x in log:
    print("Replying "+str(x))
    msg = "Hello " + str(x[1])
    comm_m.send_message_to_slave(msg, x)