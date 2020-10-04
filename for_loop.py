

for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Joe", "Joseph"]

for friend in friends:
    print(friend)

print(range(10))

for index in range(10):
    print(index)

for index in range(len(friends)):
    print(friends[index])


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))










