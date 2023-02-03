from random import *
n =randrange(1,20)
print("Computer has sucessfully generate a random number between (0,21)")

j=1
flag=0
for i in range(5,0,-1):
    print(f"\nNow, You have left {i} attempts")
    guess=int(input("Enter the number: "))
    
    if guess < n:
        print("TOO SMALL")
    
    elif guess > n:
        print("TOO BIG!")
    else:
        
        if (j == 1):
            print("\nGENIOUS- Take a BOW")
        print(f"\nYOU WIN with {j} attempts\n")
        flag=1
        break
    j+=1
if (flag == 0):
    print("\nYOU ARE A LOOSER!!\n")
