LOOKUP = {b: i for i, b in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def convert_to_denary(inputnum, frombase, tobase):
    decval = 0
    inputnumconverted = [LOOKUP[i] for i in reversed(inputnum)]
    for i, j in enumerate(inputnumconverted):
        decval += j * (frombase**i)
    output = "" 
    while decval > 0:
        remainder = decval % (tobase)
        output = str(remainder) + output
        decval = int((decval - remainder) / (tobase))
    return output

if __name__ == '__main__':
    inputnum = (input('Enter your number: '))
    frombase = int(input('In which base is your number?: '))
    tobase = int(input('To which base would you like to convert it?: '))
    print(f"Your base {frombase} number {inputnum} in base {tobase} = {convert_to_denary(inputnum, frombase, tobase)}")