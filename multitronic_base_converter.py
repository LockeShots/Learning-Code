#Converts a user-defined number from one user-defined base to another
#Highest base determined by number of possible number symbols as defined in LOOKUP

#Builds a dictionary using enumerate function on chosen order of chosen number symbols
LOOKUP = {b: i for i, b in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

#Function = 2 part process, converts user number to denary (if not already) and then from denary to specified base
#Multipliers, factors and operands derived from user-specified base values 
def convert(inputnum, frombase, tobase):
    decval = 0
    #Cconverts any extra symbols back to decimal numerals and reverses the input number
    inputnumconverted = [LOOKUP[i] for i in reversed(inputnum)]
    
    #Converts user number to denary
    for i, j in enumerate(inputnumconverted):
        decval += j * (frombase**i)
    output = "" 
    #Converts (possibly new) denary number to specified base
    while decval > 0:
        remainder = decval % (tobase)
        output = str({b: i for i, b in LOOKUP.items()}[remainder]) + output
        decval = int((decval - remainder) / (tobase))
    return output

if __name__ == '__main__':
    #Creates key variables from user input (base values converted to integers to be called later)
    inputnum = (input('Enter your number: '))
    frombase = int(input('In which base is your number?: '))
    tobase = int(input('To which base would you like to convert it?: '))
    #Prefaces output with user input and calls main function based on input
    print(f"Your base {frombase} number {inputnum} in base {tobase} = {convert(inputnum, frombase, tobase)}")