#Reads in a multi-line csv file, and allows a user to sort it by heading or/and perform a record search.
#Specifies valid commnands to check user input against.
validin = {
        'menu' : ['1','2','3','4'],
        'yesno' : ['yes','y','no','n','menu'],
        'fields' : ['First Name','Surname','Date of Birth','Address','menu'],
    }
#Creates a list of dictionaries to fill with CSV data.
listofdicts = []
f = open("task_sort_records.csv", 'r')
    #Creates a new list and fills each index with the stripped version of each seperate entry from the csv.
    #Could be done like this:
    #worklist = list(map(lambda ss: ss.strip() , worklist))
    #Haven't used this until I really understand it. =)
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

def bubbleSort(data, heading):
    has_changed = True
    while has_changed == True:
      has_changed = False
      for i in range((len(data) -1)):
        a = data[i][heading]
        b = data[i+1][heading]
        if a > b:
          data[i], data [i+1] = data [i+1], data [i]
          has_changed = True
    return data

def linearSearch(query):
    present = False
    if present == False:
         for i in listofdicts:
            if query in i.values():
                present = True
                return (f"{query} was found in the following record: {i}")
#I don't break the loop here in case the same name might be found in multiple records.
    if present == False:
        return (f"{query} was not found in the dictionary.")

if __name__ == '__main__':
    menu = True
    while menu == True:
        print ('''
        1) Sort data by heading
        2) Search for a record
        3) Print directory
        4) Quit
        ''')
        menu = False
        menuchoice = input("Please choose an option: ")
        while menuchoice not in validin['menu']:
            menuchoice = input(f"Please enter a valid number: ")
        if menuchoice == '1':
            byfield = input(f"Which field do you wish to sort by? valid inputs are {validin['fields']}: ")
            while byfield not in validin['fields']:
                byfield = input(f"Please enter {validin['fields']}: ")
            if byfield == 'menu':
                menu = True
            elif byfield in validin['fields']:
                listofdicts == bubbleSort(listofdicts, byfield)
                print("Data sorted")
                menu = True
        elif menuchoice == '2':
                query = (input('Which value do you wish to find? '))
                print(linearSearch(query))
                menu = True
        elif menuchoice == '3':
                print (listofdicts)
                menu = True
        elif menuchoice == '4':
            quit()