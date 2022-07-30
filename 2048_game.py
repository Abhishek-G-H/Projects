import random
import copy


boardsize=4
def display():
    largest=board[0][0]
    for i in board:
        for j in i:
            if(j>largest):
                largest=j
    space=len(str(largest))
    for row in board:
        curr= "|"
        for ele in row:
            if(ele == 0):
                curr += " "*space + "|"
            else:
                curr +=" "*(space-len(str(ele))) + str(ele) + "|"
        print (curr)
        print()
  

def mergeOneRowL(row):
    for i in range(boardsize):
        for j in range(boardsize-1,0,-1):
            if(row[j-1]==0):
                row[j-1]=row[j]
                row[j]=0
    for i in range(boardsize-1):
        if(row[i]==row[i+1]):
            row[i]=row[i]*2
            row[i+1]=0
    for i in range(boardsize-1,0,-1):
        if (row[i-1] == 0) :
            row[i-1]=row[i]
            row[i]=0
    return row


def mergeLeft(currboard):
    for i in range(boardsize):
        currboard[i]=mergeOneRowL(currboard[i])
    return currboard

def reverse(row):
    new=[]
    for i in range(boardsize-1,-1,-1):
        new.append(row[i])
    return new
def mergeRight(currboard):
    for i in range(boardsize):
        currboard[i]=reverse(currboard[i])
        currboard[i]=mergeOneRowL(currboard[i])
        currboard[i]=reverse(currboard[i])
    return currboard
def transpose(currboard):
    for i in range(boardsize):
        for j in range(i,boardsize):
            if (i!=j):
                temp=currboard[i][j]
                currboard[i][j]=currboard[j][i]
                currboard[j][i]=temp
    return currboard

def mergeUp(currboard):
    currboard=transpose(currboard)
    currboard=mergeLeft(currboard)
    currboard=transpose(currboard)
    return currboard

def mergeDown(currboard):
    currboard=transpose(currboard)
    currboard=mergeRight(currboard)
    currboard=transpose(currboard)
    return currboard

def pickNewVal():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2

def addNewVal():
    rowNum=random.randint(0,boardsize-1)
    colNum=random.randint(0,boardsize-1)
    while (board[rowNum][colNum]!=0):
        rowNum=random.randint(0,boardsize-1)
        colNum=random.randint(0,boardsize-1)
    board[rowNum][colNum]=pickNewVal()

def won():
    for row in board:
        if 2048 in row:
            return True
    return False

def noMoves():
    tempboard1=copy.deepcopy(board)
    tempboard2=copy.deepcopy(board)
    if(tempboard1==tempboard2):
        tempboard1=mergeLeft(tempboard1)
        if(tempboard1==tempboard2):
            tempboard1=mergeRight(tempboard1)
            if(tempboard1==tempboard2):
                tempboard1=mergeUp(tempboard1)
                if(tempboard1==tempboard2):
                    tempboard1=mergeDown(tempboard1)
                    if(tempboard1==tempboard2):
                        return True
    return False

board=[]
for i in range(boardsize):
    row=[]
    for j in range(boardsize):
        row.append(0)
    board.append(row)

numNeeded=2
while (numNeeded>0):
    rowNum=random.randint(0,boardsize-1)
    colNum=random.randint(0,boardsize-1)
    if(board[rowNum][colNum]==0):
        board[rowNum][colNum]=pickNewVal()
        numNeeded-=1

print("welcome to 2048 game : ")
print()
display()

gameOver=False

while not gameOver:
    move=input("entry direction : ")
    validInput=True
    tempboard=copy.deepcopy(board)
    if move=="d":
        mergeRight(board)
    elif move=="s":
        mergeDown(board)
    elif move=="a":
        mergeLeft(board)
    elif move=="w":
        mergeUp(board)
    else:
        validInput=False
    if not validInput:
        print("invalid input pls try again")
    else:
        if(board==tempboard):
            print("No changes!")
        elif (won()):
            gameOver=True
            print("you won!")
        else:
            addNewVal()
            display()
            if(noMoves()):
                print("No more moves, You Lost!")
                gameOver=True
    
