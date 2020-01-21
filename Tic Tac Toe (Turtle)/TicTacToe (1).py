import random
import turtle
while True: #While statement was required
    break
#Turtle setup
t = turtle
t.ht()
t.pu()
t.tracer(1,0) #Adjusts drawing speed of the turtles

#Scoreboard setup
tScore = t.Turtle()
tScore.ht()
tScore.pu()

#Sets both scores to 0
score = 0
cscore = 0

eksBoard = [] #List contains coordinates of the spots on the board with X
ohBoard = [] #Same thing with O
boardThere = ['00', '01', '02', '10', '11', '12', '20', '21', '22'] #All available board spots

def board(): #Draws the board
    t.tracer(0,0)
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
    t.tracer(1,0)

def il(x,b): #Checks if x, is in the list, b
    if x in b:
        return True

def WinCheck(b): #Returns True if all 3 winning coordinates are in a list (eksBoard and ohBoard)
    return ((il('00',b) and il('01',b) and il('02',b)) or
    (il('10',b) and il('11',b) and il('12',b)) or
    (il('20',b) and il('21',b) and il('22',b)) or
    (il('00',b) and il('10',b) and il('20',b)) or
    (il('01',b) and il('11',b) and il('21',b)) or
    (il('02',b) and il('12',b) and il('22',b)) or
    (il('00',b) and il('11',b) and il('22',b)) or
    (il('02',b) and il('11',b) and il('20',b)))

def eks(c,r): #Draws an X based on Column and Row
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

def oh(c,r): #Draws a circle based on Column and Row
    x = int(c) * 100 - 82
    y = int(r) * 100 - 82
    t.setpos(x,y)
    t.pd()
    t.circle(45)
    t.pu()

def points(winlose):
    tScore.clear() #Clears the scoreboard
    tScore.setpos(-200,50)
    tScore.write(score,align='center',font=('Arial','16','normal')) #Writes the value of score at the coordinates (-200,50)
    tScore.setpos(300,50)
    tScore.write(cscore,align='center',font=('Arial','16','normal')) #Writes the value of cscore at the coordinates (300,50)
    tScore.setpos(50,300)
    tScore.write(winlose,align='center',font=('Arial','20','bold')) #Writes the function argument at the top (You Win!, You Lose!, It's a Tie!)

def screenCheck(x,y): #When clicking on the screen, the coordinates are inputted into x and y respectively
    global clickCoords
    global score
    global cscore
    choice = []
    if x < -100 or x > 200 or y < -100 or y > 200: #If you clicked outside the tic tac toe game, the function will end
        return
    #Records where you clicked with simple 0,1,2 coordinates
    if x >= -100 and x <= 0:
        choice += '0'
    elif x > 0 and x <= 100:
        choice += '1'
    elif x > 100 and x <= 200:
        choice += '2'
    if y > -100 and y <= 0:
        choice += '0'
    elif y > 0 and y <= 100:
        choice += '1'
    elif y > 100 and y <= 200:
        choice += '2'
    #If you clicked on a square that is taken, the function will end
    if ''.join(choice) in eksBoard:
        return
    elif ''.join(choice) in ohBoard:
        return
    elif ''.join(choice) not in boardThere:
        return
    else: #If you clicked on an empty square, it will draw an X and register the coordinates
        eks(choice[0],choice[1])
        eksBoard.append(''.join(choice))
        boardThere.remove(''.join(choice))
    aiMove = False
    if WinCheck(eksBoard): #If you won, it will add 1 point to your score, declare a win and wait for a click to restart the game
        score += 1
        points('You Win!')
        t.onscreenclick(None)
        t.onscreenclick(restart)
        return
    if boardThere == []: #If there are no empty spots left, declare a tie and wait for a click to restart the game
        points('It\'s a Tie!')
        t.onscreenclick(None)
        t.onscreenclick(restart)
        return
    for i in boardThere: #Goes through every available move, and if any move results in a win, the AI will move there
        ofb = ohBoard[:]
        ofb.append(i)
        if WinCheck(ofb):
            oh(i[0],i[1])
            ohBoard.append(i)
            boardThere.remove(i)
            aiMove = True
            break
    if aiMove == False: #If the AI hasn't moved yet, it will go through every available move for you, and if any move results in a loss, the AI will try to prevent it
        for i in boardThere:
            xfb = eksBoard[:]
            xfb.append(i)
            if WinCheck(xfb):
                oh(i[0],i[1])
                ohBoard.append(i)
                boardThere.remove(i)
                aiMove = True
                break
        if aiMove == False: #If the AI still hasn't moved yet, it will select a random spot on the board and move there
            randmove = list(random.choice(boardThere))
            oh(randmove[0],randmove[1])
            ohBoard.append(''.join(randmove))
            boardThere.remove(''.join(randmove))
            aiMove = True
    if WinCheck(ohBoard): #If the AI won after it's move, it will gain a point, declare a loss and wait for a click to restart the game
        cscore += 1
        points('You Lose!')
        t.onscreenclick(None)
        t.onscreenclick(restart)
        return
    
def restart(x,y): #Restarting function will clear the board and reset the variables
    global eksBoard
    global ohBoard
    global boardThere
    t.clear()
    eksBoard = []
    ohBoard = []
    boardThere = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    board()
    points('')
    t.onscreenclick(screenCheck)
board()
points('')
t.onscreenclick(screenCheck)
t.done()
