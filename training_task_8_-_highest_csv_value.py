#Read a multiline CSV file. Print the highest number

#with open("training_task_8_-_multilinecsv.csv", 'r') as csv:
#  csvdata = csv.read()
#  numbers = csvdata.replace("\n", ",")
#  numblist = numbers.split(",")
#  numblist_int = [int(i) for i in numblist]
#print("Largest number is: ", max(numblist_int))

with open("training_task_8_-_multilinecsv.csv", 'r') as csv:
  numblist = frozenset(int(i) for i in ((csv.read()).replace("\n", ",")).split(","))
print(f"Largest number is: {max(numblist)}")