#Create a list from the alphabet.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#This function compares each letter in user input with alphabet list
#to find the correct index value for that letter.
def getindex(wordletter):
    """
    >>> getindex('a')
    0
    >>> getindex('z')
    25
    """
    newindexvalue = (alphabet.index(wordletter))
    return newindexvalue

#Asks for a word and an offset. Applies cypher based on offset and returns shifted string.
def caesar_cypher(word, offset):
    """
    >>> caesar_cypher('abc', 1)
    'bcd'
    >>> caesar_cypher('hello', 1)
    'ifmmp'
    >>> caesar_cypher('ifmmp', -1)
    'hello'
    >>> caesar_cypher('xyz', 1)
    'yza'
    >>> caesar_cypher('z a b', 1)
    'a b c'
    """
    outputlist = []
    for wordletter in word:
        if wordletter in alphabet:
            newindexvalue = int(getindex(wordletter)) + int(offset)
            newindexvalue = (newindexvalue % len(alphabet))
            new_letter = alphabet[newindexvalue]
            outputlist.append(new_letter)
    return (''.join(outputlist))

if __name__ == "__main__":
    output = caesar_cypher(input("Enter word to be cipherized: "), input("Enter cipher calculation: "))
    print(output)