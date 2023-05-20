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