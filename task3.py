numberlist = list(range(0, 30))

print('The numbers between 0 and 30 not divisible by 4 are: ')
for item in numberlist:
    if item % 4 != 0:
        print(item)