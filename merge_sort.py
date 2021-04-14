def comparator (key, a,b):
    return a[key] > b[key]
    print

def listfromstring(datatosort):
    return list(datatosort)

def halver(listtosplit):
    middle = len(listtosplit)//2
    while middle >= 2:
    L = listtosplit[:middle]
    R = listtosplit[middle:]
    halver(L)
    halver(R)
    
#def mergeSort(data):
    #datalist = list([i] for i in (list(data)))
    #print(datalist)
    #pairSort(datalist)
    #quadSort(pairlist)

if __name__ == '__main__':
    numbers = "14619358857468597"
    datalist = listfromstring(numbers)
    print(halver(datalist))