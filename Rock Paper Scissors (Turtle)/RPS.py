from random import *
import turtle

global userScore
global compScore

userScore = 0
compScore = 0

tr = turtle #Alias the turtle as tr for faster typing
tr.tracer(1,0) #Increases the speed for the turtle
tr.pu() #Turtle doesn't draw when it moves
tr.ht() #Hide the turtle

def rock(d): #Draw a hand like a rock. The d variable dictates which
#                                      direction the rock is facing.
    tr.pd()
    tr.pencolor("blue")
    tr.fd(40*d)
    tr.lt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(10*d)
    tr.bk(10*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(10*d)
    tr.bk(10*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(10*d)
    tr.bk(10*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(40*d)
    tr.bk(30*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(30*d)
    tr.pu()
def scissors(d): #Draw a hand like scissors
    tr.pd()
    tr.pencolor("green")
    tr.fd(30*d)
    tr.lt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(15*d)
    tr.bk(15*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(15*d)
    tr.bk(15*d)
    tr.rt(180*d)
    tr.fd(20*d)
    tr.lt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(30*d)
    tr.bk(30*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(50*d)
    tr.bk(20*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(20*d)
    tr.pu()
def paper(d): #Draw a hand like paper
    tr.pd()
    tr.pencolor("red")
    tr.fd(60*d)
    tr.lt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(30*d)
    tr.bk(30*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(30*d)
    tr.bk(30*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(30*d)
    tr.bk(30*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(60*d)
    tr.bk(30*d)
    tr.rt(90*d)
    tr.fd(10*d)
    tr.lt(90*d)
    tr.fd(30*d)
    tr.bk(30*d)
    tr.rt(90*d)
    tr.pu()
def square(color): #Draw a square with a specific color
    tr.pd()
    tr.color(color)
    tr.fd(50)
    tr.rt(90)
    tr.fd(50)
    tr.rt(90)
    tr.fd(50)
    tr.rt(90)
    tr.fd(50)
    tr.pu()

def textDisplay(text): #Displays the text variable at the top of the screen
    tr.home()
    tr.setpos(0,100)
    tr.pd()
    tr.color('black')
    tr.write(text,False,align="center",font=("Arial",12,"normal"))
    tr.pu()

def box():
    #Draw a blue square that says "Rock"
    tr.home()
    tr.setpos(-100,-100)
    square('blue')
    tr.setpos(-74,-132)
    tr.write("Rock",False,align="center")

    #Draw a red square that says "Paper"
    tr.home()
    tr.setpos(-25,-100)
    square('red')
    tr.setpos(1,-132)
    tr.write("Paper",False,align="center")

    #Draw a green square that says "Scissors"
    tr.home()
    tr.setpos(50,-100)
    square('green')
    tr.setpos(76,-132)
    tr.write("Scissors",False,align="center")

def checkClick(x,y):
    global userScore
    global compScore
    #Checks if the user clicks within each of the squares
    if -150 < y < -100:
        if -100 < x < -50:
            choice = 1
        elif -25 < x < 25:
            choice = 2
        elif 50 < x < 100:
            choice = 3
        else:
            return
        turtle.onscreenclick(None) #Stops checking for screen clicks
        tr.clear() #Clear screen
        compChoice = randint(1,3) #Selects a random integer between 1 and 3 for use as the computers choice

        
        #Draw either rock paper or scissors based upon what was chosen
        tr.home()
        tr.setpos(-100,0)
        if choice == 1:
            rock(1)
        elif choice == 2:
            paper(1)
        elif choice == 3:
            scissors(1)
            
        #Draws rock paper or scissors
        tr.home()
        tr.setpos(100,0)
        if compChoice == 1:
            rock(-1)
        elif compChoice == 2:
            paper(-1)
        elif compChoice == 3:
            scissors(-1)

        #Displays text based upon whether you won, lost or drew the match
        if compChoice == choice:
            textDisplay("Draw!")
        elif compChoice == choice-1 or compChoice == choice+2:
            textDisplay('You Win!')
            userScore += 1
        else:
            textDisplay("You Lose!")
            compScore += 1
        tr.setpos(-200,15)
        tr.write("User Score:",False,align="center")
        tr.setpos(-200,0)
        tr.write(userScore,False,align="center")
        tr.setpos(200,15)
        tr.write("Computer Score:",False,align="center")
        tr.setpos(200,0)
        tr.write(compScore,False,align="center")
        box()
        turtle.onscreenclick(checkClick)

box()
turtle.onscreenclick(checkClick) #Sends the coordinates of when you click on the screen, to the function, checkClick
turtle.done()
