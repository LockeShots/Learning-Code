pricing = {'b': 29.99, 'p': 49.99, 'exhaustpipe': 69.99}

def jobprice(tyrenum, tyretype, ispipereq):
    """
    >>> jobprice(1, 'b', 'n')
    29.99
    >>> jobprice(1, 'b', 'y')
    89.98
    >>> jobprice(1, 'p', 'n')
    49.99
    >>> jobprice(1, 'p', 'y')
    109.98
    >>> jobprice(5, 'b', 'y')
    179.95
    >>> jobprice(6, 'b', 'n')
    'You have exceeded the maximum number of tyres'
    >>> jobprice(5, 'g', 'y')
    'Tyre type must be 'b' or 'p''
    """
    totalprice = ""
    if tyrenum <= 3:
        totalprice = (pricing[tyretype] * tyrenum)
    if tyrenum >= 4:
        totalprice = (pricing[tyretype] * tyrenum) * 0.8
    if ispipereq == 'y':
        totalprice += (pricing['exhaustpipe'])
    if tyrenum > 0 and ispipereq == 'y':
        totalprice -= 10
    return round(totalprice, 2)

if __name__ == '__main__':
    tyrenum = int(input('How many tyres are required (max 5)? '))
    tyretype = (input('Are (b)udget or (p)remium tyres required? '))
    ispipereq = (input('Is an exhaust pipe required, y/n? '))
    print(f"The total price is: £{jobprice(tyrenum, tyretype, ispipereq)}")