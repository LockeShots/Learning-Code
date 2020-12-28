#Generate the fibonacci sequence

num1 = 1
num2 = 2

count = 0
while count < 11:
    count = count + 1
    num1 = num1 + 1
    num2 = num1 + num2
    print(num1 + num2)