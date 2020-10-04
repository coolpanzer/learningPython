# r = read
# w = write

employee_file = open("employees.txt", "r")

#print(employee_file.readable())
#print(employee_file.readline())
#print(employee_file.readlines()[2])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

#appending

employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human resources")
employee_file.close()

#write a file

employee_file = open("employees.txt", "w")
employee_file.write("\njopit - Human resources")
employee_file.close()