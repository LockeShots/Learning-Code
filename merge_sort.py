import math
def pairSort(datalist):
    #print(datalist)
    P = 0
    #Creates a list of lists, and a number of empty lists within the pair list
    #equal to the number of items in the dataset / 2 (one list for each sorting pair)
    num_of_pairs = (math.ceil((len(datalist)) / 2))
    print(num_of_pairs)
    #print (num_of_pairs)
    pairlist = list([] for i in (range(num_of_pairs)))
    #print(pair)
    #current_pair variable decides which pair is being built - Will increment until all data
    #in initial dataset parsed into sorted pairs
    current_pair = 0
    while P < len(datalist):
        if datalist[P] < datalist[P+1]:
            pairlist[current_pair].append(datalist[P])
            pairlist[current_pair].append(datalist[P+1])
        else:
            pairlist[current_pair].append(datalist[P+1])
            pairlist[current_pair].append(datalist[P])
        P += 2
        current_pair += 1
    print(pairlist)
    return pairlist

def mergeSort(data):
    datalist = list([i] for i in (list(data)))
    #print(datalist)
    pairSort(datalist)
    #quadSort(pairlist)


if __name__ == '__main__':
    numbers = "14619358857468597"
    #print(numbers)
    mergeSort(numbers)

#    pl = 0
#    pr = 0
#        while (data left to sort):
#            quadnum = 0
#            while (quad(quadnum) has less than 4 values)
#                if pair(pairnum)(pl) > pair(pairnum+1)(pr):
#                    append pair(pairnum+1)(pr) to quad(quadnum)
#                    pr += 1
#            else:
#                append pair(pairnum+1)(pr) to quad(quadnum)
#                pl += 1
#        quadnum += 1