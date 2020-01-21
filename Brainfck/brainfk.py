import re
import turtle
from math import sqrt

str = open("code.bf", "r").read()
lochar = re.findall("[><+-.,\[\]]", str) + [""]


# Takes valid BF code and outputs a tuple of dictionaries, where the first dicitonary
#   links open indices with closed, and the second does the reverse
# linkBrackets: BFCode -> ({openToClose}, {closeToOpen})
def linkBrackets(code):
    openBrackets = []
    closedBrackets = []

    openToClose = {}
    closeToOpen = {}

    for i in range(len(code)):
        if code[i] == "[":
            openBrackets.append(i)
        elif code[i] == "]":
            openIndex = openBrackets.pop()
            openToClose[openIndex] = i
            closeToOpen[i] = openIndex

    # for closeIndex in closedBrackets:
    #     openIndex = openBrackets[i]

    #     openToClose[openIndex] = closeIndex
    #     closeToOpen[closeIndex] = openIndex
    
    return (openToClose, closeToOpen)

def step():
    global charIndex, pointer
    char = lochar[charIndex]

    if char == ">":
        pointer += 1

    elif char == "<":
        pointer -= 1

    elif char == "+":
        if tape[pointer] == 255:
            tape[pointer] = 0
        else:
            tape[pointer] += 1

    elif char == "-":
        if tape[pointer] == 0:
            tape[pointer] = 255
        else:
            tape[pointer] -= 1

    elif char == ".":
        print(chr(tape[pointer]), end="")

    elif char == ",":
        tape[pointer] = ord(input()[0])

    elif char == "[" and tape[pointer] == 0:
        charIndex = openToClose[charIndex]
        pass

    elif char == "]" and tape[pointer] != 0:
        charIndex = closeToOpen[charIndex]
        pass

    charIndex += 1

tape = [0 for i in range(10000)]         # Tape of bytes
pointer = 0                             # Pointer points at bytes
charIndex = 0                           # Index of the current character (could be replaced?)

links = linkBrackets(lochar)
openToClose = links[0]
closeToOpen = links[1]

def drawTape(t,size):
    global tape
    tapeLength = ([0] + [i for i, e in enumerate(tape, 1) if e != 0])[-1]

    t.clear()
    t.pu()
    t.goto(0, 500)
    t.pd()

    for i in range(tapeLength):
        t.fd(size)
        t.rt(90)
        t.fd(size)
        t.rt(90)
        t.fd(size)
        t.rt(90)
        t.fd(size)
        t.rt(90)

        t.pu()
        t.rt(45)
        t.fd(sqrt(2 * size**2) / 2)

        t.write(tape[i], align="center")

        t.lt(90)
        t.fd(sqrt(2 * size**2) / 2)
        t.rt(45)
        t.pd()

def drawPointer(t, size):
    global pointer
    t.seth(90)
    t.pu()
    x = size / 2 + pointer * size
    y = 500 - size - 20
    t.goto(x, y)

turtle.setworldcoordinates(-10,-10,510,510)

tapeTurtle = turtle.Turtle()
pointerTurtle = turtle.Turtle()

turtle.tracer(1,0)

while lochar[charIndex] != "":
    step()
    drawTape(tapeTurtle, 30)
    drawPointer(pointerTurtle, 30)
turtle.done()
