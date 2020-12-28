def bubbleSort(data):
    """
    >>> bubbleSort(['c','b','d'])
    ['b', 'c', 'd']
    """

#    print('bubbleSort')
    has_changed = True
    while has_changed == True:
#      print (data)
      has_changed = False
      for i in range((len(data) -1)):
        a = data[i]
        b = data[i+1]
#        print("Comparing" a "with" b)
        if a > b:
#          print("swap")
          data[i] = b
          data[i+1] = a
          has_changed = True
    return data

if __name__ == '__main__':
    data = [
    'lady',
    'squiggly',
    'mcfugglenugget',
    'crabbledobs',
    'punter',
    'the',
    'third',
    'bob'
    ]
    data = bubbleSort(data)
    print(data)