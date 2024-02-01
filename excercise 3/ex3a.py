# Write a python program to find factorial of a number using Recursion.
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


num = int(input("enter a number: "))
print("factorial of given number is ", fact(num))
