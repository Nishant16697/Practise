def pa():
    n=input("Please enter only one alphabet :  ")
    t1=n.upper()
    if len(t1) !=1:
        print("No. of input is not 1")
    else:
        if not t1.isalpha():
            print("Enter response is not alphabet")
        else:

            # A
            if t1=="A":
                for i in range(9):
                    for j in range(9):
                        if ((i==0 or i==6) and (j==3 or j==4 or j==5))  or (j >= 1 or j<=9) and (i!=0 and (j==2 or j==6)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print()

            # B
            if t1=="B":
                for i in range(9):
                    for j in range(9):
                        if ((i==0 or i==4  or i==8) and (j==3 or j==2 or j==4))   or (i!=9 and (j==1)) or (j==5 and (i!=0 and i!=4  and i!=8)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print()

            # C
            if t1=="C":
                for i in range(9):
                    for j in range(9):
                        if ((i!=0 and i!=9  and i!=8) and (j==1))   or (j==5 and (i==7 or i==1)) or ((j==3 or j==4 or j==2) and (i==8 or i==0)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print()


            # D
            if t1=="D":
                for i in range(9):
                    for j in range(9):
                        if (j==1)  or (j==5 and (i<=7 and i>=1)) or ((j==2 or j==3 or j==4) and (i==0 or i==8)) :
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print()


            # E
            if t1=="E":
                for i in range(9):
                    for j in range(9):
                        if (j==1)  or ((i==4 or i==0 or i==8) and (j<=5 and j>=1)) :
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print()   


            # F
            if t1=="F":
                for i in range(9):
                    for j in range(9):
                        if (j==1)  or ((i==4 or i==0) and (j<=5 and j>=1)) :
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 


            # G
            if t1=="G":
                for i in range(9):
                    for j in range(9):
                        if ((j==3 or j==5) and (i==6)) or ((j==1) and (i>=2 and i<=6)) or (i==5 and (j<=5 and j>=3)) or ((j==3 or j==4) and (i==0 or i==8)) or ((i==1 or i==7) and (j==2 or j==5)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 


            # H
            if t1=="H":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==5) and (i!=0 and i<=7)) or (i==4 and (j>=1 and j<=5)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 



            # I
            if t1=="I":
                for i in range(9):
                    for j in range(9):
                        if ((j==4) and (i!=0 and i<=7)) or ((i==1 or i==7) and (j>=2 and j<=6)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 


            # J
            if t1=="J":
                for i in range(9):
                    for j in range(9):
                        if ((j==5) and (i!=0 and i<=6)) or ((i==1) and (j>=2 and j<=8)) or ((j==3 or j==4) and i==7) or (j==2 and i==6):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # K
            if t1=="K":
                for i in range(9):
                    for j in range(9):
                        if ((j==1) and (i!=0 and i<=7)) or ((i==4) and (j==2)) or ((i==2 or i==6) and (j==3) or ((i==1 or i==7) and (j==4))):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # L
            if t1=="L":
                for i in range(9):
                    for j in range(9):
                        if ((j==1) and (i!=0 and i<=7)) or ((i==7) and (j>=1 and j<=4)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # M
            if t1=="M":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==7) and (i!=0 and i<=7)) or ((i==2) and (j==2 or j==6)) or ((i==3) and (j==3 or j==5)) or ((i==4) and (j==4)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # N
            if t1=="N":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==7) and (i!=0 and i<=7)) or ((i==2) and (j==2)) or ((i==3) and (j==3)) or ((i==4) and (j==4)) or ((i==5) and (j==5)) or ((i==6) and (j==6)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 


            # O
            if t1=="O":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==5) and (i>=2 and i<=5)) or ((j>=2 and j<=4) and (i==1 or i==6)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 


            # P
            if t1=="P":
                for i in range(9):
                    for j in range(9):
                        if ((j==1) and (i>=0 and i<=7)) or ((j>=1 and j<=4) and (i==0 or i==4)) or ((i>=1 and i<=3) and (j==5)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # Q
            if t1=="Q":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==6) and (i>=2 and i<=5)) or ((j>=2 and j<=5) and (i==1 or i==6)) or (i==5 and j==4) or (i==6 and j==5) or (i==7 and j==6):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # R
            if t1=="R":
                for i in range(9):
                    for j in range(9):
                        if ((j==1) and (i>=0 and i<=7)) or ((j>=1 and j<=4) and (i==0 or i==4)) or ((i>=1 and i<=3) and (j==5)) or (j==2 and i==5) or (j==3 and i==6) or (j==4 and i==7):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # S
            if t1=="S":
                for i in range(9):
                    for j in range(9):
                        if ((j>=1 and j<=5) and (i==1 or i==7 or i==4)) or (j==0 and (i==2 or i==3)) or (j==6 and (i==5 or i==6)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print()


            # T
            if t1=="T":
                for i in range(9):
                    for j in range(9):
                        if ((j==4) and (i!=0 and i<=7)) or ((i==1) and (j>=2 and j<=6)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # U
            if t1=="U":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==5) and (i!=0 and i<=6)) or ((j>=2 and j<=4) and i==7):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # V
            if t1=="V":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==7) and (i==1)) or ((i==2) and (j==2 or j==6)) or ((i==3) and (j==3 or j==5)) or ((i==4) and (j==4)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 


            # W
            if t1=="W":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==7) and (i!=0 and i<=7)) or ((i==6) and (j==2 or j==6)) or ((i==5) and (j==3 or j==5)) or ((i==4) and (j==4)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 


            # X
            if t1=="X":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==7) and (i==1)) or ((i==2) and (j==2 or j==6)) or ((i==3) and (j==3 or j==5)) or ((i==4) and (j==4)) or ((j==1 or j==7) and (i==7)) or ((i==6) and (j==2 or j==6)) or ((i==5) and (j==3 or j==5)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print()


            # Y
            if t1=="Y":
                for i in range(9):
                    for j in range(9):
                        if ((j==1 or j==7) and (i==1)) or ((i==2) and (j==2 or j==6)) or ((i==3) and (j==3 or j==5)) or ((i>=4) and (i<=7) and (j==4)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 

            # Z
            if t1=="Z":
                for i in range(9):
                    for j in range(9):
                        if ((i==1 or i==7) and (j!=0 and j<=7)) or ((i==2) and (j==6)) or (i==3 and  j==5) or ((i==4) and (j==4)) or ((i==5) and (j==3)) or ((i==6) and (j==2)):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print() 


pa()