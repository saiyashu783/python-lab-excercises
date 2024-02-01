# Write a program that inputs a text file. The program should print all of the
# unique words in the file in alphabetical order.

import string

file = open("unique.txt")
text = file.read()
text = text.lower()
for var in string.punctuation:
    text = text.replace(var, "")
words = text.split()
words = sorted(set(words))
print(words)
print("count of unique words: ", len(words))
