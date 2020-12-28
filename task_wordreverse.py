#Joint task - Open file, reverse letters in words preserving word order and write back to file.

f = open("task_wordreverse_text.txt", 'r')
for line in f:
    line = line.split(" ")
    linereverse = [i[::-1] for i in line]
    linereverse_string = ' '.join(linereverse)
with open("task_wordreverse_text.txt", 'a') as f:
    f.truncate(0)
    f.write(linereverse_string)
exit