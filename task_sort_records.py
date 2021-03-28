from functools import partial
import operator

#Reads in a multi-line csv file, and allows a user to sort it by heading or/and perform a record search.
#Specifies valid commnands to check user input against.
validin = {
    'menu' : ('1','2','3','4'),
    'yesno' : ('yes','y','no','n','menu'),
    'fields' : ('First Name','Surname','Date of Birth','Address','menu'),
}

def load_data(filename="task_sort_records.csv", func_open=open):
    #Creates a list of dictionaries to fill with CSV data.
    listofdicts = []
    f = func_open(filename, 'r')
        #Creates a new list and fills each index with the stripped version of each seperate entry from the csv.
        #Could be done like this:
        #worklist = list(map(lambda ss: ss.strip() , worklist))
        #Haven't used this until I really understand it. =)
    
    # Header rwo in CSV??
    #line = f.readline???() ?? dont know?
    #??heading processin

    for line in f:
        d = {}
        worklist = [item.strip() for item in line.split("|")]
        #This creates a dictionary with heading names as keys for each line of CSV and appends it to the list of dictionaries.
        listofdicts.append({
            "First Name": worklist[0],
            "Surname": worklist[1],
            "Date of Birth": worklist[2],
            "Address": worklist[3],
        })
    return listofdicts

listofdicts = load_data()


def printDict(d):
    """
    The cleandict strips the null values from any dictionary sent here.
    Put this here instead of making a new function so I can apply it to nested dictionaries directly.
    Not sure why it isn't working!"""
    d = {k: v for k, v in d.items() if k is not None}
    for key, value in d.items():
        print(key, ' : ', value)

def _dict_key_comparator(key, a,b):
    return a[key] > b[key]
#def _default_comparator(a, b):
#    return _dict_key_comparator('Forename', a, b)
#_default_comparator = partial(_dict_key_comparator, 'Forename')

def bubbleSort(data, func_comparison=operator.gt):
    """
    >>> bubbleSort(['c','b','a'])
    ['a','b','c']
    >>> bubbleSort([3,2,1])
    [1,2,3]
    >>> bubbleSort([3,2,1], func_comparison=operator.lt)
    [3,2,1]
    >>> bubbleSort([{'a': 1, 'b':2}, {'a':4, 'b':3}], lambda a, b: a['b'] > b['b'])
    [{'a':4, 'b':3}, {'a': 1, 'b':2}]
    """
    has_changed = True
    while has_changed == True:
      has_changed = False
      for i in range((len(data) -1)):
        #a = data[i][heading]
        #b = data[i+1][heading]
        a = data[i]
        b = data[i+1]
        #if a > b:
        if func_comparison(a, b):
          data[i], data [i+1] = b, a  #data [i+1], data [i]
          has_changed = True
    return data

def linearSearch(query):
    present = False
    if present == False:
        for i in listofdicts:
            for key, value in i.items():
                if query in value:
                    present = True
                    #Wanted to use "{(printDict(i))}" here, but it printed the record before the print statement, not sure why.
                    return (f"{query} was found in the {key} field of the following record:{i}")
#I don't break the loop here in case the same name might be found in multiple records.
    if present == False:
        return (f"{query} was not found in the dictionary.")

if __name__ == '__main__':
    #Sets a boolean variable menu to True, and uses a conditional while loop to print menu options before setting menu to false,
    #to prevent recursive loop.
    menu = True
    while menu == True:
        print ('''
        Welcome to Locke's CSV parsing program. Please select one of the following options:

        1) Sort data by heading
        2) Search for a record
        3) Print directory
        4) Quit
        ''')
        menu = False
        menuchoice = input("Please choose an option: ")
        #Thought about building a dictionary of functions and calling a given function directly based on the menu number entered.
        #Seemed more complicated than it was worth.
        while menuchoice not in validin['menu']:
            menuchoice = input(f"Please enter a valid number: ")
        if menuchoice == '1':
            #Need a way of stripping the formatting from this dictionary call.
            byfield = input(f"Which field do you wish to sort by? valid inputs are {validin['fields']}: ")
            while byfield not in validin['fields']:
                byfield = input(f"Please enter {validin['fields']}: ")
            if byfield == 'menu':
                #Anytime menu becomes 'True' again, main menu screen is printed once and process restarts.
                menu = True
            elif byfield in validin['fields']:
                listofdicts == bubbleSort(listofdicts, partial(_dict_key_comparator, byfield))
                print("Data sorted")
                menu = True
        elif menuchoice == '2':
                query = (input('Which value do you wish to find? '))
                #I would like to print this result neatly with 'Record (index number)' about it. Also have it work for multiple records
                #containing the same value.
                print(linearSearch(query))
                menu = True
        elif menuchoice == '3':
                #This will take into account any amount of sorting and resorting that has been performed.
                count = 1
                for i in listofdicts:
                    print (f'''
                    Record {count}
                    ''')
                    print (printDict(i))
                    count += 1
                menu = True
        elif menuchoice == '4':
            quit()

  #  menu_items_strings = ''.join(
  #      f'    {key}: {value}\n'
  #      for key, value in menu_items.items()
  #  )