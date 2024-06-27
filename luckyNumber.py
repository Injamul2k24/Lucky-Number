
import random
N = int(input(" Enter a positive number : "))
if N == 0:
    print("You enter :", 0)
    print("Enter a positive number between 1 to infinite ")
elif N > 0 :
    random_number = random.randint(1, N)
    print("Hurrah! your lucky number is : ",random_number)
    print("Thank You For Visiting :")
elif N < 0 :
    print("You enter a negative number  :")
    print("Enter a positive number between 1 to infinite ")
    
else:
    print("You enter a invalid number or syntax")
    print("Enter a positive number between 1 to infinite ")
    