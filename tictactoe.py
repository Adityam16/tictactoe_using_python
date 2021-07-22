import random
m=3
n=3
z=1
l=0
a=[[random.random()for row in range(3)]for col in range(3)]
for i in range(m):
    for j in range(n):
        a[i][j]=z
        z=z+1
print(" Numbers Represent Position U Want To Insert X or O")
for o in range(m):
    for p in range(n):
        print(a[o][p],"  ",end=" ")
    print()
print("Remember Positions")
name1=input("Enter Player 1 name and player 1 will have X ")
name2=input("Enter Player 2 name and player 2 will have O ")
while True:
    l=l+1
    print("Player 1 turn")
    n=int(input("Enter position U want to insert X"))
    if n==1:
        a[0][0]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif n==2:
        a[0][1]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif n==3:
        a[0][2]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif n==4:
        a[1][0]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif n==5:
        a[1][1]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif n==6:
        a[1][2]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif n==7:
        a[2][0]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif n==8:
        a[2][1]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif n==9:
        a[2][2]="X"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    else:
        print("Enter Valid Input Next Time")
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    if ((a[0][0]=="X" and a[0][1]=="X" and a[0][2]=="X")or(a[1][0]=="X" and a[1][1]=="X" and a[1][2]=="X")or(a[2][0]=="X" and a[2][1]=="X" and a[2][2]=="X") or (a[0][0]=="X" and a[1][0]=="X" and a[2][0]=="X")or(a[0][1]=="X" and a[1][1]=="X" and a[2][1]=="X")or(a[0][2]=="X" and a[1][2]=="X" and a[2][2]=="X")or(a[0][0]=="X" and a[1][1]=="X" and a[2][2]=="X")or(a[0][2]=="X" and a[1][1]=="X" and a[2][0]=="X")):
        print(name1,"IS WINNER***************")
        break
    if l==9:
        print("DRAW*************")
        break
    print("Player 2 Turn")
    m=int(input("Enter position U want to insert O"))
    l=l+1
    if m==1:
        a[0][0]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif m==2:
        a[0][1]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif m==3:
        a[0][2]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif m==4:
        a[1][0]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif m==5:
        a[1][1]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif m==6:
        a[1][2]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif m==7:
        a[2][0]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif m==8:
        a[2][1]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    elif m==9:
        a[2][2]="O"
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    else:
        print("Enter Valid Input Next Time")
        for b in range(3):
            for c in range(3):
                print(a[b][c],"  ",end=" ")
            print()
    if ((a[0][0]=="O" and a[0][1]=="O" and a[0][2]=="O")or(a[1][0]=="O" and a[1][1]=="O" and a[1][2]=="O")or(a[2][0]=="O" and a[2][1]=="O" and a[2][2]=="O") or (a[0][0]=="O" and a[1][0]=="O" and a[2][0]=="O")or(a[0][1]=="O" and a[1][1]=="O" and a[2][1]=="O")or(a[0][2]=="O" and a[1][2]=="O" and a[2][2]=="O")or(a[0][0]=="O" and a[1][1]=="O" and a[2][2]=="O")or(a[0][2]=="O" and a[1][1]=="O" and a[2][0]=="O")):
        print(name2,"IS WINNER***************")
        break
print(" ")
print(" ")
print("SUMMARY OF GAME:")
    
for q in range(3):
    for r in range(3):
        print("_",end="")
        print(a[q][r],"|",end="")
    print()













        
    
