import math
#Day 1, Advent of Code

def conv(mass):
    x = math.floor(mass / 3) - 2
    if x <= 0:
        return 0
    else:
        return x

f = open("data.txt", "r")

lines = f.readlines()

f = 0
tf = 0

#computes the total fuel needed including the mass of the fuel itself
def total_added_fuel(mass):
    f = conv(mass)
    tf = f
    while f > 1:
        f = conv(f)
        tf += f
    return tf

req1 = 0
req2 = 0

for line in lines:
    req1 += conv(int(line))
    req2 += total_added_fuel(int(line))

#req1 prints the total fuel to be added using the nominal mass
#req2 prints the total fuel to be added using the weight of the fuel itself
print(req1)
print(req2)



