#Converts a binary value into a denary value
def Bin2Dec(binaryvalue):
    """
    >>> Bin2Dec('1101')
    11
    >>> Bin2Dec('11101')
    23
    """
    output = 0
    factor = 1
    #Progresses through the reversed binary string and multiplies each index by the factor
    for i in range(len(binaryvalue)):
        output += int(binaryvalue[i]) * factor
    #Increases the factor by a power of 2 each loop
        factor = factor * 2
    return output

if __name__ == '__main__':
    #Takes user inport and reverses it
    binaryvalue = (input('Enter a binary number to convert to denary: ')[::-1])
    print(f"Denary value = {Bin2Dec(binaryvalue)}")