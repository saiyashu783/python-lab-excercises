# Write a Python class to implement pow(x, n)
class Power:
    def pow(self, a, b):
        result = 1
        for i in range(0, b):
            result *= a
        return result


base = int(input("enter base number: "))
exp = int(input("enter exp number: "))
print("result: ", Power().pow(base, exp))
