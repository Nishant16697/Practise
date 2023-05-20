# A

for i in range(9):
    for j in range(9):
        if ((i==0 or i==6) and (j==3 or j==4 or j==5))  or (j >= 1 or j<=9) and (i!=0 and (j==2 or j==6)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()

# B

for i in range(9):
    for j in range(9):
        if ((i==0 or i==4  or i==8) and (j==3 or j==2 or j==4))   or (i!=9 and (j==1)) or (j==5 and (i!=0 and i!=4  and i!=8)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()

# C
for i in range(9):
    for j in range(9):
        if ((i!=0 and i!=9  and i!=8) and (j==1))   or (j==5 and (i==7 or i==1)) or ((j==3 or j==4 or j==2) and (i==8 or i==0)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()


# D
for i in range(9):
    for j in range(9):
        if (j==1)  or (j==5 and (i<=7 and i>=1)) or ((j==2 or j==3 or j==4) and (i==0 or i==8)) :
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()


# E
for i in range(9):
    for j in range(9):
        if (j==1)  or ((i==4 or i==0 or i==8) and (j<=5 and j>=1)) :
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()   


    # F
for i in range(9):
    for j in range(9):
        if (j==1)  or ((i==4 or i==0) and (j<=5 and j>=1)) :
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 


# G
for i in range(9):
    for j in range(9):
        if ((j==3 or j==5) and (i==6)) or ((j==1) and (i>=2 and i<=6)) or (i==5 and (j<=5 and j>=3)) or ((j==3 or j==4) and (i==0 or i==8)) or ((i==1 or i==7) and (j==2 or j==5)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 


# H
for i in range(9):
    for j in range(9):
        if ((j==1 or j==5) and (i!=0 and i<=7)) or (i==4 and (j>=1 and j<=5)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 



# I
for i in range(9):
    for j in range(9):
        if ((j==4) and (i!=0 and i<=7)) or ((i==1 or i==7) and (j>=2 and j<=6)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 


# J
for i in range(9):
    for j in range(9):
        if ((j==5) and (i!=0 and i<=6)) or ((i==1) and (j>=2 and j<=8)) or ((j==3 or j==4) and i==7) or (j==2 and i==6):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# K
for i in range(9):
    for j in range(9):
        if ((j==1) and (i!=0 and i<=7)) or ((i==4) and (j==2)) or ((i==2 or i==6) and (j==3) or ((i==1 or i==7) and (j==4))):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# L
for i in range(9):
    for j in range(9):
        if ((j==1) and (i!=0 and i<=7)) or ((i==7) and (j>=1 and j<=4)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# M
for i in range(9):
    for j in range(9):
        if ((j==1 or j==7) and (i!=0 and i<=7)) or ((i==2) and (j==2 or j==6)) or ((i==3) and (j==3 or j==5)) or ((i==4) and (j==4)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# N
for i in range(9):
    for j in range(9):
        if ((j==1 or j==7) and (i!=0 and i<=7)) or ((i==2) and (j==2)) or ((i==3) and (j==3)) or ((i==4) and (j==4)) or ((i==5) and (j==5)) or ((i==6) and (j==6)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 


# O
for i in range(9):
    for j in range(9):
        if ((j==1 or j==5) and (i>=2 and i<=5)) or ((j>=2 and j<=4) and (i==1 or i==6)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 


# P
for i in range(9):
    for j in range(9):
        if ((j==1) and (i>=0 and i<=7)) or ((j>=1 and j<=4) and (i==0 or i==4)) or ((i>=1 and i<=3) and (j==5)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# Q
for i in range(9):
    for j in range(9):
        if ((j==1 or j==6) and (i>=2 and i<=5)) or ((j>=2 and j<=5) and (i==1 or i==6)) or (i==5 and j==4) or (i==6 and j==5) or (i==7 and j==6):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# R
for i in range(9):
    for j in range(9):
        if ((j==1) and (i>=0 and i<=7)) or ((j>=1 and j<=4) and (i==0 or i==4)) or ((i>=1 and i<=3) and (j==5)) or (j==2 and i==5) or (j==3 and i==6) or (j==4 and i==7):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# S
for i in range(9):
    for j in range(9):
        if ((j>=1 and j<=5) and (i==1 or i==7 or i==4)) or (j==0 and (i==2 or i==3)) or (j==6 and (i==5 or i==6)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()


# T
for i in range(9):
    for j in range(9):
        if ((j==4) and (i!=0 and i<=7)) or ((i==1) and (j>=2 and j<=6)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# U
for i in range(9):
    for j in range(9):
        if ((j==1 or j==5) and (i!=0 and i<=6)) or ((j>=2 and j<=4) and i==7):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# V
for i in range(9):
    for j in range(9):
        if ((j==1 or j==7) and (i==1)) or ((i==2) and (j==2 or j==6)) or ((i==3) and (j==3 or j==5)) or ((i==4) and (j==4)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 


# W
for i in range(9):
    for j in range(9):
        if ((j==1 or j==7) and (i!=0 and i<=7)) or ((i==6) and (j==2 or j==6)) or ((i==5) and (j==3 or j==5)) or ((i==4) and (j==4)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 


# X
for i in range(9):
    for j in range(9):
        if ((j==1 or j==7) and (i==1)) or ((i==2) and (j==2 or j==6)) or ((i==3) and (j==3 or j==5)) or ((i==4) and (j==4)) or ((j==1 or j==7) and (i==7)) or ((i==6) and (j==2 or j==6)) or ((i==5) and (j==3 or j==5)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()


# Y
for i in range(9):
    for j in range(9):
        if ((j==1 or j==7) and (i==1)) or ((i==2) and (j==2 or j==6)) or ((i==3) and (j==3 or j==5)) or ((i>=4) and (i<=7) and (j==4)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 

# Z
for i in range(9):
    for j in range(9):
        if ((i==1 or i==7) and (j!=0 and j<=7)) or ((i==6) and (j==6)) or (i==5 and  j==5) or ((i==4) and (j==4)) or ((i==3) and (j==3)) or ((i==2) and (j==2)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print() 