# Write a program to count the numbers of characters in the string and store
# them in a dictionary data structure

string = input("enter a string: ")
print("total characters in the string: ", len(string))
d = {}
for i in string:
    d[i] = string.count(i)
print(d)
