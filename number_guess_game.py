import random
cp = random.randint(1, 10)
lifes = 5
while lifes != 0:
    user = int(input("ENTER THE NUMBER: "))  
    if user < cp:
        lifes -= 1
        print(f"{user} is too low,{lifes} remaing chances")
    elif user > cp:
        lifes -= 1
        print(f"{user} is too high,{lifes} remaining chances")  
    else:
        print("CORRECT GUESS")
        break
else:
    print(f"OUT OF CHANCES, {cp} is correct guess")