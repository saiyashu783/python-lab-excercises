# Write a function dups to find all duplicates in the list.

def dups(x):
    unique = set()
    duplicate = []
    for num in x:
        if num not in unique:
            unique.add(num)
        else:
            duplicate.append(num)
    return duplicate


data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 8, 9, 10]
duplicates = dups(data)
if duplicates:
    print("Duplicate elements:", duplicates)
else:
    print("No duplicates found.")
