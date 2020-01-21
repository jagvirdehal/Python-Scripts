from random import *
import turtle
import time
t = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
ball = turtle.Turtle()
ball.shape("circle")
paddleSpeed = 20
def speedReset():
    global ballSpeed
    ballSpeed = [1,1]
    ballSpeed = [uniform(3,4)*2*(ballSpeed[0]/abs(ballSpeed[0])),uniform(3,4)*2*(ballSpeed[1]/abs(ballSpeed[1]))]
speedReset()
turtle.tracer(30,0)
t.ht()
b.ht()
c.ht()
ball.ht()
t.pu()
b.pu()
c.pu()
ball.pu()
def pong(x,y):
    ball.setpos(x,y)
    ball.pd()
    ball.clear()
    ball.color('white')
    ball.begin_fill()
    ball.circle(2)
    ball.end_fill()
    ball.pu()
def ballMove():
    global ballSpeed
    pong(ball.xcor()+ballSpeed[0],ball.ycor()+ballSpeed[1])
    if ball.ycor() > 120 or ball.ycor() < -120:
        ballSpeed[1] *= -1
    if ball.xcor() > 200:
        ballSpeed[0] *= -1
        speedReset()
        pong(0,0)
    if ball.xcor() < -200:
        ballSpeed[0] *= -1
        speedReset()
        pong(0,0)
    if 195 < ball.xcor() < 200 and c.ycor()-20 < ball.ycor() < c.ycor()+20:
        ballSpeed[0] *= -1
    if -200 < ball.xcor() < -195 and t.ycor()-20 < ball.ycor() < t.ycor()+20:
        ballSpeed[0] *= -1
def boundary():
    b.seth(0)
    b.setpos(0,-120)
    b.pd()
    b.color('black')
    b.begin_fill()
    b.fd(200)
    b.lt(90)
    b.fd(240)
    b.lt(90)
    b.fd(400)
    b.lt(90)
    b.fd(240)
    b.lt(90)
    b.fd(200)
    b.end_fill()
    b.pu()
def paddle(x,y):
    t.setpos(-200,y)
    t.color('white')
    t.seth(90)
    t.pd()
    t.begin_fill()
    t.fd(20)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(20)
    t.end_fill()
    t.pu()
def down():
    t.clear()
    paddle(t.xcor(),t.ycor()-paddleSpeed)
    if t.ycor() > 100:
        t.setpos(t.xcor(),100)
        t.clear()
        paddle(t.xcor(),t.ycor())
    elif t.ycor() < -100:
        t.clear()
        t.setpos(t.xcor(),-100)
        paddle(t.xcor(),t.ycor())
def up():
    t.clear()
    paddle(t.xcor(),t.ycor()+paddleSpeed)
    if t.ycor() > 100:
        t.setpos(t.xcor(),100)
        t.clear()
        paddle(t.xcor(),t.ycor())
    elif t.ycor() < -100:
        t.clear()
        t.setpos(t.xcor(),-100)
        paddle(t.xcor(),t.ycor())
def comp(x,y):
    c.setpos(195,y)
    c.color('white')
    c.seth(90)
    c.pd()
    c.begin_fill()
    c.fd(20)
    c.rt(90)
    c.fd(5)
    c.rt(90)
    c.fd(40)
    c.rt(90)
    c.fd(5)
    c.rt(90)
    c.fd(20)
    c.end_fill()
    c.pu()
def compMove():
    if ball.ycor() > c.ycor():
        c.setpos(c.xcor(),c.ycor()+(ballSpeed[1]/2))
        c.clear()
        comp(c.xcor(),c.ycor())
    elif ball.ycor() < c.ycor():
        c.setpos(c.xcor(),c.ycor()-(ballSpeed[1]/2))
        c.clear()
        comp(c.xcor(),c.ycor())
    ballMove()
boundary()
comp(0,0)
paddle(0,0)
pong(0,0)
turtle.onkey(down,"Down")
turtle.onkey(up,"Up")
turtle.onkey(down,"s")
turtle.onkey(up,"w")
start_time = time.time()
turtle.listen()
while True:
    time.sleep(0.05)
    compMove()
