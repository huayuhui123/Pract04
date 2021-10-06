numbers=[]
for time in range(0,5,1):
    number=int(input("Number:"))
    numbers.append(number)
print("The first number is",numbers[0])
print("The last number is",numbers[4])
print("The smallest number is",min(numbers))
print("The largest number is",max(numbers))
print("The average of the numbers is {}".format(sum(numbers)/5))
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username=input("What's your name?")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")