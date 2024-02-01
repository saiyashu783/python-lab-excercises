# Write a function unique to find all the unique elements of a list.

# ERRORS ?????

# def uniq(x):
#    unique = set(x)
#    return list(unique)


def uniq(x):
    unique = set()
    duplicate = []
    for num in x:
        if num not in unique:
            unique.add(num)
        else:
            unique.remove(num)
    return unique


data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 8, 9, 10]
uniques = uniq(data)
if uniques:
    print("unique elements:", uniques)
else:
    print("No unique element found.")
