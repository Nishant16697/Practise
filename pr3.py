for i in range(9):
    for j in range(9):
        if ((i==0 or i==6) and (j==3 or j==4 or j==5))  or (j >= 1 or j<=9) and (i!=0 and (j==2 or j==6)):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()


