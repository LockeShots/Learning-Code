#Read a list of numbers from a file. Print the sum of all the numbers.

f = open("training_task_2_-_numblist", 'r')
numbers = f.read()
numbsplit = numbers.split()
numbsplit_int = [int(i) for i in numbsplit]
listsum = sum(numbsplit_int)
print(listsum)
