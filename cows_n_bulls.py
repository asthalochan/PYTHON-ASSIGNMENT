from maskpass import * #for hide number by coder (run in terminal pip install maskpass)
from random import * 

print("-: Welcome to Cows and Bulls Game :-")
def computer():
    while True:
        try:
            num=randint(1000,9999)
            computer_list=[int(x) for x in str(num)]
            if (len(computer_list) == 4) and (computer_list[0] != computer_list[1] != computer_list[2] != computer_list[3]):
                break
        except:
            pass
    print("Computer has sucessfully guessed the number")
    return computer_list

def person():
    print("\nHey...!")
    while True:
        try:
            num =askpass(prompt="Enter 4 digit number with all different digits :", mask=" *")
            coder_list = [int(x) for x in str(num)]
            if (len(coder_list) == 4) and (coder_list[0] != coder_list[1] != coder_list[2] != coder_list[3]):
                break
        except:
            pass

    print("You have sucessfully guessed the number")
    return coder_list

def cracker():
    print("\nHey Cracker,guess the number...!")
    while True:
        try:
            num1 =input("Enter a valid four digit number:")
            cracker_list=[int(x) for x in str(num1)]
            if (len(cracker_list) == 4):
                break
        except:
            pass
    return cracker_list
    
def cow(list1,list2):
    cow=0
    for i in range (len(list1)):
        for j in range(len(list1)):
            if (list1[i] == list2[j]):
                if i!=j:
                    cow+=1
    return cow

def bull(list1,list2):
    bull=0
    for i in range (len(list1)): 
        if list1[i] == list2[i]:
            bull+=1
    return bull

while True:
    print("\n-: MAIN MENU :-")
    print("1.Computer v/s Person")
    print("2.Person v/s Person")
    print("3.Exit")
    choice=int(input("\nEnter Your Choice:"))

    if choice == 1:
        computer_num=computer()
        cracker_num=cracker()
        cow_s=cow(computer_num,cracker_num)
        bull_s=bull(computer_num,cracker_num)
        print(f"\nScores: {cow_s} Cow and {bull_s} Bull ")
    elif choice == 2:
        person_num=person()
        cracker_num=cracker()
        cow_s=cow(person_num,cracker_num)
        bull_s=bull(person_num,cracker_num)
        print(f"\nScores: {cow_s} Cow and {bull_s} Bull ")
    elif choice == 3:
        break
    else:
        print("\nOops! Incorrect Choice.")
        

