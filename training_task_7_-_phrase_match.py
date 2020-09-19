#Read in a phrase from a user. If the phrase exists in a file print “Phrase exists”
#This should ignore case

filename = "phrases.txt"
with open(filename) as f:
    phrasefile = f.read()
phrase = input("Type a phrase: ")
if phrase.lower() in phrasefile.lower():
    print(phrase)
else:
    print("Phrase does not exist in file.")