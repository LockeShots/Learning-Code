listofdicts = []
f = open("project_recordsearch_data.csv", 'r')
for line in f:
    d = {}
    worklist = line.split("|")
    index = 0
    while index < len(worklist):
      worklist[index] = worklist[index].strip()
      index += 1
    #print (worklist)
    d.update({"First Name": worklist[0]})
    d.update({"Surname": worklist[1]})
    d.update({"Date of Birth": worklist[2]})
    d.update({"Address": worklist[3]})
    listofdicts.append(d)
    
print (listofdicts)