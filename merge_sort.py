def comparator (key, a,b):
    return a[key] > b[key]
    print

def listfromstring(datatosort):
    return list(datatosort)

def halver(listtosplit):
    middle = len(listtosplit)//2
    return middle
    
#def mergeSort(data):
    #datalist = list([i] for i in (list(data)))
    #print(datalist)
    #pairSort(datalist)
    #quadSort(pairlist)

if __name__ == '__main__':
    numbers = "14619358857468597"
    datalist = listfromstring(numbers)
    print(halver(datalist))