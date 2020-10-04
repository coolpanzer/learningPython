

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divide 0")
except ValueError as err:
    print(err)