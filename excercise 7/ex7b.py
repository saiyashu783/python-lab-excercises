# Write a program to count frequency of characters in a given file. Can you use
# character frequency to tell whether the given file is a Python program file, C
# program file or a text file?

file = open("hello.py", "r")
text = file.read()
print("total characters in the string: ", len(text))
d = {}
for i in text:
    d[i] = text.count(i)
print(d)

# no we can't use character frequency to tell whether the given file
# is a Python program file, C program file or a text file.