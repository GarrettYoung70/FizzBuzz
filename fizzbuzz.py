# For loop that checks each value from 1 to 100 and prints according to the condition
for value in range(1, 101):
    # Checks if the value is divisible by 3 or 5 and prints FizzBuzz if it is and continues back to the top
    if value % 3 == 0 and value % 5 == 0:
        print("FizzBuzz")
        continue
    # Checks if the value is divisible by 3 and prints Fizz if it is and continues back to the top
    elif value % 3 == 0:
        print("Fizz")
        continue
    # Checks if the value is divisible by 5 and prints Buzz if it is and continues back to the top
    elif value % 5 == 0:
        print("Buzz")
        continue
    # Prints the value if it does not meet any of the other conditions
    print(value)