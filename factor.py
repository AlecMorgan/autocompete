import fileinput

import math


for line in fileinput.input():
    n = int(line)
    factors = []
    while n%2==0:
        factors.append(2)
        n=n/2
    
    for i in range(3, int(math.sqrt(n))+1,2):
        while n%i == 0:
            factors.append(i)
            n=int(n/i)

    if n>2:
        factors.append(n)

factors = list(map(int, factors))
#print(factors)
factors = sorted(factors, reverse=True)
#print(factors)

factors_print = "*".join(list(map(str, factors)))

print(factors_print)