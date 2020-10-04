
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male or tall")
elif is_male and not(is_tall):
    print("Maybe")
else:
    print("You are a female")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= 3:
        return num1
    elif num2 >= num1 and num2 >= 3:
        return num2
    else:
        return 3

print(max_num(3,5,4))
