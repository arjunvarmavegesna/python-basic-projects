print("CREATED BY ARJUN VARMA")
print("WANNA CALCULATE SOMETHING!")
user1 = input("WHAT DO YOU WANT TO CALCULATE + - * / : ")
user2 = input("ENTER THE NUMBER YOU WANT TO CALCULATE: ")
while user1 == "+" or user1 == "-" or user1 == "*" or user1 == "/":
    if user1 == "+":
        numbers = list(map(int, user2.split()))
        total = sum(numbers)
        print(total)
        break
    elif user1 == "-":
        numbers = list(map(int, user2.split()))
        result = numbers[0]
        for n in numbers[1:]:
         result -= n
        print(result)
        break
    elif user1 == "*":
       numbers = list(map(int, user2.split()))
       result = numbers[0]
       for n in numbers[1:]:
         result *= n
       print(result)
       break
    elif user1 == "/":
        numbers = list(map(int, user2.split()))
        result = numbers[0]
        for n in numbers[1:]:
         result /= n
        print(result)
        break
print("THANK YOU!")