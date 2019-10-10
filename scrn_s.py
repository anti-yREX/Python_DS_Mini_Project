from graphics import *

def initiate(id):
    win = GraphWin("Window id : "+str(id),400,550)
    return win

def animate(win):
    cir = Circle(Point(425,225),25)
    cir.setFill("#2771c4")
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
    cir.setFill("#2771c4")
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