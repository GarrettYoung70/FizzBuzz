for value in range(1, 101):
    if value % 3 == 0 and value % 5 == 0:
        print("FizzBuzz")
        continue
    elif value % 3 == 0:
        print("Fizz")
        continue
    elif value % 5 == 0:
        print("Buzz")
        continue
    print(value)