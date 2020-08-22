#Ask user for 5 words
#Create world salad using between 10-20 random words from input

import random
x = random.randint(10, 21)
while True:
    words = input("Enter 5 random words seperated by commas: ")
    userwordlist = words.split(", ")
    if len(userwordlist) == 5:
        print(random.choices(userwordlist, k=x))
        break
    print("Please enter exactly 5 words and make sure to seperate them with commas: ")