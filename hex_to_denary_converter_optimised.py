#aa = [
#    int(x)
#    for x in range(10)
#]
bb = {
    0: 'a',
    1: 'b',
}

for key, value in bb.items():
    print(f'{key} = {value}')

def get_base(x):
    return '1234235t3shevfjskzdvsukefbsugharg'[0:x]

def hex2dec(hexvalue, base):
    """
    >>> hex2dec('0', '01')
    0
    
    """
    LOOKUP = {h: i for i, h in enumerate(base)}
    output = 0
    for i, h in enumerate(LOOKUP[j] for j in reversed(hexvalue)):
        output += h * (len(LOOKUP)**i)
    return output

if __name__ == '__main__':
    #Takes user input
    hexvalue = input('Enter a hex number to convert to denary: ')
    base = input('what base: ')
    print(f"Denary value = {Hex2Dec(hexvalue, base='0123456789abcdef')}")