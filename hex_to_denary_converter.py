hexdic = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
    }

def Hex2Dec(hexvalue):
    hexvalue = hexvalue[::-1]
    hex2decvalue = []
    output = 0 
    for i in range(len(hexvalue)):
        hex2decvalue.append(hexdic[hexvalue[i]])

    for i in range(len(hex2decvalue)):  
        output += hex2decvalue[i] * (16**i)
    return output

if __name__ == '__main__':
    #Takes user input
    hexvalue = (input('Enter a hex number to convert to denary: '))
    print(f"Denary value = {Hex2Dec(hexvalue)}")