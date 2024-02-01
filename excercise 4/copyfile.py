#  Write a script named copyfile.py. This script should prompt the user for the
# names of two text files. The contents of the first file should be input and
# written to the second file.

file1 = input("enter file name 1: ")
file2 = input("enter file name 2: ")
f1 = open(file1, "w")
f1.write(input("enter some dummy lines: "))
f1.close()
f1 = open(file1)
f2 = open(file2, "w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()
f2 = open(file2)
print(f2.read())
f2.close()

# import shutil
# shutil.copyfile("original.txt", "copy.txt")