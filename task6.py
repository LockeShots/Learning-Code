timeinput = input("Please enter a 12h time with the format 0:00am/pm: ")
twelvehour = timeinput.split(":")
if 'a' in twelvehour:
    twelvehour[1] = twelvehour[1][:-2]
    print(*twelvehour, sep = ':')
if 'p' in twelvehour:
    twelvehour[1] = twelvehour[1][:-2]
    twelvehour[0] = int(twelvehour[0])+12
    print(*twelvehour, sep = ':')
else:
    print("Check input for am/pm.")
    exit