
print("Rule\n- If the player’s number is divisible by 3 then the player says **fizz** instead of their number.\n- If the player’s number is divisible by 5 then the player says **buzz** instead of their number.\n- A player must say **fizz buzz** for numbers that are divisible by both 3 and 5.    ")
number=int(input("Insert:"))
while number <= 100:

    if number%3==0 and number%5==0:
        print("buzzfizz")
    elif number%5==0:
        print("buzz")
    elif number%3==0:
        print("fizz")
    else:
        print(number)
    number=int(input())