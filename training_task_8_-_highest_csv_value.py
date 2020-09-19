#Read a multiline CSV file. Print the highest number

with open("multilinecsv.csv", 'r') as csv:
  csvdata = csv.read()
  numbers = csvdata.replace("\n", ",")
  numblist = numbers.split(",")
  numblist_int = [int(i) for i in numblist]
print("Largest number is: ", max(numblist_int))