#Ask user for statement
#If statement begins with 's', print to file

def print_input():
    f = open("s-statement.txt", 'a')
    f.write (statement + "\n")
    f.close ()

statement = input("Enter Statement: ")
result = statement.startswith('s')
if (result) == True:
    print_input()
else:
    exit