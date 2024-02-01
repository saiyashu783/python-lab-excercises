# Write a Python program to convert temperatures to and from Celsius,
# Fahrenheit [Formula: c/5 = f-32/9]

temp = float(input("enter temperature: "))
units = input("C or F: ")
if units.upper() == "C":
    con_temp = (9*temp/5)+32
    print("temperature in fahrenheit: ", con_temp, " F")
elif units.upper() == "F":
    con_temp = (temp-32)*5/9
    print("temperature in celsius: ", con_temp, " C")
else:
    print("enter the correct units")
