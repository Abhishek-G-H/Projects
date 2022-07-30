from operator import truediv
import re
import turtle
import time
import math

def drawboard():
    for i in range(2):
        drawer.penup()
        drawer.goto(-300,100-200*i)
        drawer.pendown()
        drawer.forward(600)
    drawer.right(90)
    for j in range(2):
        drawer.penup()
        drawer.goto(-100+200*j,300)
        drawer.pendown()
        drawer.forward(600)
    num=1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j*200 , 280 - i*200)
            drawer.pendown()
            drawer.write(num,font=("Arial",12))
            num+=1
    screen.update()

def drawX(x,y):
    drawer.penup()
    drawer.goto(x,y)
    drawer.pendown()
    drawer.setheading(60)
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)
    screen.update()
    
def drawO(x,y):
    drawer.penup()
    drawer.goto(x,y+75)
    drawer.pendown()
    drawer.setheading(0)
    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)
    screen.update()

def checkwon(letter):
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2]==letter):
            return True
        if(board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[2][i]==letter):
            return True
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==letter):
        return True
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==letter):
        return True
    return False

def checktie():
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=="x":
                count+=1
    
    if count>3:
        return True
    else:
        return False
    

def addO():
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                board[i][j]="o"
                if checkwon("o"):
                    drawO(-200+200*j,200-200*i)
                    return
                board[i][j]=" "
                
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                board[i][j]="x"
                if checkwon("x"):
                    board[i][j]="o"
                    drawO(-200+200*j,200-200*i)
                    return
                board[i][j]=" "
    for i in range(0.3,2):
        for j in range(0,3,2):
            board[i][j]="o"
            drawO(-200+200*j,200-200*i)
            return
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                board[i][j]="o"
                drawO(-200+200*j,200-200*i)
                return
            
            

def activate():
    for i in range(9):
        screen.onkey(functions[i],str(i+1))

def deactivate():
    for i in range(9):
        screen.onkey(None,str(1+i))
    

def addX(row,col):
    if board[row][col]=="x" or board[row][col]=="o":
        announcer.write("That spot is taken!",font=("Arial",36))
        screen.update()
    else:
        drawX(-200+200*col,200-200*row)
        board[row][col]="x"
        if checkwon("x"):
            announcer.goto(-97,0)
            announcer.write("You Won!",font=("Arial",36))
            screen.update()
            deactivate()
        else:
            addO()
            if checkwon("o"):
                announcer.goto(-97,0)
                announcer.write("You Lost!",font=("Arial",36))
                screen.update()
                deactivate()
            elif checktie():
                announcer.goto(-97,0)
                announcer.write("It's a Tie!",font=("Arial",36))
                screen.update()
                deactivate()
            

def sqone():
    addX(0,0)
def sqtwo():
    addX(0,1)
def sqthree():
    addX(0,2)
def sqfour():
    addX(1,0)
def sqfive():
    addX(1,1)
def sqsix():
    addX(1,2)
def sqseven():
    addX(2,0)
def sqeight():
    addX(2,1)
def sqnine():
    addX(2,2)

functions=[sqone,sqtwo,sqthree,sqfour,sqfive,sqsix,sqseven,sqeight,sqnine]


    
drawer=turtle.Turtle()
announcer=turtle.Turtle()
announcer.penup()
announcer.goto(-200,0)
announcer.color("red")
drawer.pensize(10)
drawer.ht()
screen=turtle.Screen()
screen.tracer(0)

drawboard()

board=[]
for i in range(3):
    row=[]
    for j in range (3):
        row.append(" ")
    board.append(row)

time.sleep(5)