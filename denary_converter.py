def Bin2Dec(binary):
    output = 0
    operand = 1
    index = -1
    outputlist = []
    while abs(index) <= len(binary):
        output = int(binary[(index)]) * operand
        outputlist.append(output)
        index = index - 1
        operand = operand * 2
    return sum([int(i) for i in outputlist])

binaryvalue = (input('Enter a binary number to convert to denary: '))
print(f"Denary value = {Bin2Dec(binaryvalue)}")