from maskpass import * #for hide number by coder (run in terminal pip install maskpass)
print("Hey Coder...!")
while True:
    try:
        num =askpass(prompt="Enter a valid four digit number:", mask=" #")
        coder_list = [int(x) for x in str(num)]
        if (len(coder_list) == 4):
            break
    except:
        pass
print("Hey Cracker,guess the number...!")
while True:
    try:
        num1 =input("Enter a valid four digit number:")
        cracker_list=[int(x) for x in str(num1)]
        if (len(cracker_list) == 4):
            break
    except:
        pass
cow=0
for i in range (len(coder_list)):
    for j in range(len(coder_list)):
        if (coder_list[i] == cracker_list[j]):
            if i!=j:
                cow+=1
bull=0
for i in range (len(coder_list)):
    if coder_list[i] == cracker_list[i]:
        bull+=1
print(f"Scores: {cow} Cow and {bull} Bull ")