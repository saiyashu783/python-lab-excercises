# Write a function nearly equal to test whether two strings are nearly equal.
# Two strings a and b are nearly equal when a can be generated by a single
# mutation on b.

def nearly_equal(a, b):
    if len(a) != len(b):
        return False
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff <= 1


x = "abc"
y = "adc"
if nearly_equal(x, y):
    print("nearly equal.")
else:
    print("not nearly equal.")
