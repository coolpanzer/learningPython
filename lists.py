
friends = ["kevin", "rev", "ryah","joey"]

print(friends)
print(friends[1])
print(friends[1:])
print(friends[1:3])

lucky_numbers = [4, 7, 9, 10, 23, 43, 50]

friends.append("rima")
friends.insert(1, "ranz")
friends.extend(lucky_numbers)
friends.remove("kevin")

#Remove last element of the list
friends.pop()

friends.index("joey")

friends.count("rima")

lucky_numbers.sort()
lucky_numbers.reverse()

super_friends = friends.copy()

print(super_friends)

