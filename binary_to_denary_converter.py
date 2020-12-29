#Converts a binary value into a denary value
def Bin2Dec(binaryvalue):
    """
    >>> Bin2Dec('1101')
    13
    >>> Bin2Dec('11101')
    29
    """
    binaryvalue = binaryvalue[::-1]
    output = 0
    #Progresses through the reversed binary string and multiplies each index by 2 * the factor of the index
    for i in range(len(binaryvalue)):
        output += int(binaryvalue[i]) * (2**i)
    return output

if __name__ == '__main__':
    #Takes user inport and reverses it
    binaryvalue = (input('Enter a binary number to convert to denary: '))
    print(f"Denary value = {Bin2Dec(binaryvalue)}")