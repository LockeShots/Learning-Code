LOOKUP = {b: i for i, b in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def convert_to_denary(inputnum, base):
    """
    >>> 
    """
    inputnumconverted = [LOOKUP[i] for i in reversed(inputnum)]
    output = 0
    for i, j in enumerate(inputnumconverted):
        output += j * (base**i)
    #for i in range(len(inputnumconverted)):
    #    output += inputnumconverted[i] * ((base)**i)
    return output

if __name__ == '__main__':
    #Takes user input
    inputnum = (input('Enter a number to convert to denary: '))
    base = int(input('In which base is your number?: '))
    print(f"Number in specified base = {convert_to_denary(inputnum, base)}")