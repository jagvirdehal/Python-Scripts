import turtle
t = turtle
t.ht()
t.pu()
t.tracer(0,0)

column = ['0','1','2']
row = ['0','1','2']

boardTaken = []
boardThere = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
boardSpots = {'00', '01', '02', '10', '11', '12', '20', '21', '22'}
print(boardSpots)
##for c in column:
##    for r in row:
##        boardThere.append(c+r)
print(boardThere)
def board():
    t.setpos(0,-100)
    t.seth(90)
    t.pd()
    t.fd(300)
    t.pu()
    t.setpos(100,-100)
    t.seth(90)
    t.pd()
    t.fd(300)
    t.pu()
    t.setpos(-100,0)
    t.seth(0)
    t.pd()
    t.fd(300)
    t.pu()
    t.setpos(-100,100)
    t.seth(0)
    t.pd()
    t.fd(300)
    t.pu()

def WinCheck():
    print()

def eks(c,r):
    x = int(c) * 100 - 50
    y = int(r) * 100 - 50
    t.setpos(x,y)
    t.pd()
    t.seth(45)
    t.fd(50)
    t.bk(100)
    t.setpos(x,y)
    t.seth(-45)
    t.fd(50)
    t.bk(100)
    t.pu()

def screenCheck(x,y):
    global clickCoords
    global boardTaken
    global boardThere
    choice = []
    if x < -100 or x > 200 or y < -100 or y > 200:
        return
    if x >= -100 and x <= 0:
        choice += column[0]
    elif x > 0 and x <= 100:
        choice += column[1]
    elif x > 100 and x <= 200:
        choice += column[2]
    if y > -100 and y <= 0:
        choice += row[0]
    elif y > 0 and y <= 100:
        choice += row[1]
    elif y > 100 and y <= 200:
        choice += row[2]
    if (choice[0] + choice[1]) in boardTaken:
        return
    else:
        eks(choice[0],choice[1])
        boardTaken.append(''.join(choice))
        boardThere.remove(''.join(choice))
        print(boardThere)
        print(boardTaken)

board()
t.onscreenclick(screenCheck)
