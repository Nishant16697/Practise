def palandrome():
    n=input("Enter a number:")
    if n == n[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

palandrome()
