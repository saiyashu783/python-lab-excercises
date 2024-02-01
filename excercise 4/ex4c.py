# Write a Python class to convert an integer to a roman numeral.

class RomanNum:
    def int_to_roman(self, x):
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = 12
        roman_x = ""
        while x != 0:
            if num[i] <= x:
                roman_x += roman[i]
                x = x - num[i]
            else:
                i -= 1
        return roman_x


number = int(input("enter a number: "))
print("In roman numeral: ", RomanNum().int_to_roman(number))