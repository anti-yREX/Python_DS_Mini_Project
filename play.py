"""
#Experiment for MultiThreading

import threading
st = ""
def func1():
    id = 1
    n = 0
    while n!=10:
        print(id)
        print(gmtime())
        n+=1
    return

def func2():
    id = 2
    n = 0
    while n!=10:
        print(id)
        print(gmtime())
        n+=1
    return

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.start()
t2.start()
t1.join()
t2.join()
"""

"""
#Experiment for Time Based Exection

from time import gmtime

def add_time(t1,t2):
     t3 = [0,0]
     t3[1] = ( t1[1] + t2[1] ) % 60
     t3[0] = ( t1[0] + t2[0] ) + ((t1[1] + t2[1])//60)
     return t3

n = 5
c_t = gmtime()
c_tm = [c_t[4], c_t[5]]
print(c_tm)

ex_tm = [0, 5]
ex_tm = add_time(c_tm,ex_tm)
print("Command: Slave 0: Start Execution on " + str(ex_tm))

for i in range(1,5):
    ex_tm = add_time(ex_tm,[0,11])
    print("Command: Slave "+ str(i) +": Start Execution on "+str(ex_tm))

ex_tm = add_time(ex_tm,[0,11])
print("Master: Start its on execution "+ str(ex_tm))
"""

