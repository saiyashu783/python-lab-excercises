# Write a program that accepts the lengths of three sides of a triangle as
# inputs. The program output should indicate whether the triangle is a
# right triangle (Recall from the Pythagorean Theorem that in a right triangle,
# the square of one side equals the sum of the squares of the other two sides).

def is_rtangle(x, y, z):
    sides = sorted([x, y, z])
    if sides[2]**2 == sides[1]**2 + sides[0]**2:
        return True
    else:
        return False


a = int(input("enter value of first side: "))
b = int(input("enter value of second side: "))
c = int(input("enter value of third side: "))
if is_rtangle(a, b, c):
    print("the triangle is right angled. ")
else:
    print("the triangle is not right angled. ")
