# Write a Python script that prints prime numbers less than 20.

import math
for n in range(2, 20):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            break
        i = i+1
    if i > math.sqrt(n):
        print(n)
