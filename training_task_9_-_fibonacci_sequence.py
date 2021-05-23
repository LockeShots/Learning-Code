#Generate the fibonacci sequence

def fibseq(limit):
    """
    >>> fibseq('10')
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    """
    fiblist = list()
    fiblist.append(i+(i+1) for i in range(0, (limit)))
    return(fiblist)

if __name__ == '__main__':
    limit = int(input("To how many digits would you like to determine the fibonacci sequence?: "))
    print(f"{fibseq(limit)}")