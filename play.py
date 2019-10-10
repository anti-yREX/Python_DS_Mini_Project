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

for i in range(1,n):
    ex_tm = add_time(ex_tm,[0,11])
    print("Command: Slave "+ str(i) +": Start Execution on "+str(ex_tm))

ex_tm = add_time(ex_tm,[0,11])
print("Master: Start its on execution "+ str(ex_tm))
"""

"""
#Experiment: Convert Message to Executable Time
msg = "[25,26]"
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
    tm = (int(min) , int(sec))
    return tm
tm = decode_time(msg)
print(tm)
"""
from graphics  import *
from time import gmtime

def initiate(id):
    win = GraphWin("Window id : "+str(id),400,550)
    return win

def animate(win):
    cir = Circle(Point(425,225),25)
    cir.setFill("#000000")
    cir.setOutline("#000000")
    cir.draw(win)
    n = 425
    while n > (-30):
        for i in range(1,98000):
            continue
        cir.move(-1,0)
        n -= 1

    for i in range(1,98000):
            continue

    cir = Circle(Point(425,225),25)
    cir.setFill("#d11800")
    cir.setOutline("#000000")
    cir.draw(win)
    n = 425
    while n > (-30):
        for i in range(1,98000):
            continue
        cir.move(-1,0)
        n -= 1
        
    for i in range(1,98000):
            continue

    cir = Circle(Point(425,225),25)
    cir.setFill("#000000")
    cir.setOutline("#000000")
    cir.draw(win)
    n = 425
    while n > (-30):
        for i in range(1,98000):
            continue
        cir.move(-1,0)
        n -= 1
    win.close()
    return

win = initiate(2)
s_t=gmtime()
s_t = (s_t[4],s_t[5])
animate(win)
e_t=gmtime()
e_t = (e_t[4],e_t[5])
print(str(s_t)+" "+str(e_t))