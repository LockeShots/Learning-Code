list_of_dicts = []
with open("project_recordsearch_data.csv", 'r') as csv:
for line in csv:
    worklist = line.split("|")
    worklist = list(map(lambda ss: ss.strip() , worklist))
    list_of_dicts.append({
        "First Name": worklist[0],
        "Surname": worklist[1],
        "Date of Birth": worklist[2],
        "Address": worklist[3],
    })
    
print (list_of_dicts)