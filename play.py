import threading
st = ""
def func1():
    id = 1
    n = 0
    while n!=100:
        s = "Hello from "+ str(id) +" #"+ str(n)
        print(s)
        st = str(id) + str(n)
        print(st)
        n+=1
    return

def func2():
    id = 2
    n = 0
    while n!=100:
        s = "Hello from "+ str(id) +" #"+ str(n)
        print(s)
        st = str(id) + str(n)
        print(st)
        n+=1
    return

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.start()
t2.start()
t1.join()
t2.join()