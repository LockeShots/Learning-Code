listofdicts = []
csv = open("project_recordsearch_data.csv", 'r')
for line in csv:
    csvdict = {}
    worklist = line.split("|")
    index = 0
    while index < len(worklist):
      worklist[index] = worklist[index].strip()
      index += 1
    csvdict.update({"First Name": worklist[0]})
    csvdict.update({"Surname": worklist[1]})
    csvdict.update({"Date of Birth": worklist[2]})
    csvdict.update({"Address": worklist[3]})
    listofdicts.append(csvdict)
    
print (listofdicts)