#def Dec2Bin(denary):
#  output = ""
#  while denary > 0:
#    remainder = denary % 2
#    output = str(remainder) + output
#    denary = int((denary - remainder) / 2)
#  return output
  
#thenumber = int(input('enter a number to convert: '))
#print(f"Binary value = {Dec2Bin(thenumber)}")

"""
>>> Bin2Dec(1)
1
"""

def Bin2Dec(binary):
    output = 0
    operand = 1
    index = -1
    while index <= len(binary):
        output = binary[(index)] * operand
        index = index - 1
        operand = operand * 2
    return output

binaryvalue = (input('Enter a binary number to convert to denary: '))
print(f"Denary value = {Bin2Dec(binaryvalue)}")