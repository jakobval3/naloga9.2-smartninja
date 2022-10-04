print("This is FizzBuzz, a fun game for everyone!")

user_input= int(input("Please enter a whole number between 1 and 100 here:"))

for x in range(1,(user_input+1)):
    if (x % 3) != 0 and (x % 5) != 0:
        print(x)
    elif (x % 3) == 0 and (x % 5) == 0:
        print("FizzBuzz")
    elif (x % 3) == 0:
        print("Fizz")
    elif (x % 5) == 0:
        print("Buzz")


