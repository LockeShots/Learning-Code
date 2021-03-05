#Reads in a multi-line csv file, and allows a user to sort it by heading or/and perform a record search.

listofdicts = []
f = open("task_sort_records.csv", 'r')
for line in f:
    d = {}
    worklist = [item.strip() for item in line.split("|")]
    #Creates a new list and fills each index with the stripped version of each seperate entry from the csv.
    #Could be done like this:
    #worklist = list(map(lambda ss: ss.strip() , worklist))
    #haven't used this until I really understand it. =)

    #This creates a dictionary with heading names as keys for each line of CSV and appends it to a list of dictionaries.
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

def linearsearch(query):
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
    validyn = ['yes','y','no','n','exit']
    validbyfield = ['First Name','Surname','Date of Birth','Address','exit']
    bsort = (input('Do you wish to sort data? Valid inputs are "yes", "y", "no", or "n": '))
    while bsort not in validyn:
        bsort = (input('Please enter "yes", "y", "no", or "n" or type "exit" to quit: '))
    if bsort == 'exit':
        quit()
    if bsort == 'yes' or bsort == 'y':
        byfield = (input('Which field do you wish to sort by? Valid inputs are "First Name", "Surname", "Date of Birth" or "Address": '))
        while byfield not in validbyfield:
            byfield = (input('Please enter "First Name", "Surname", "Date of Birth" or "Address" or type "exit" to quit: '))
        if byfield == 'exit':
            quit()
        if byfield in validbyfield:
            listofdicts == bubbleSort(listofdicts, byfield)
    search = (input('Do you want to search the records?: '))
    while search not in validyn:
        search = (input('Please enter "yes", "y", "no", or "n" or type "exit" to quit: '))
    if search == 'exit':
        quit()
    if search == 'yes' or search == 'y':
        query = (input('Which value do you wish to find? '))
        print(linearsearch(query))
    if search == 'no' or search == 'n':
        quit()