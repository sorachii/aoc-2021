#!/usr/bin/env python3

gamma   = ["0" for _ in range(12)]
epsilon = ["0" for _ in range(12)]
counter = [0 for _ in range(12)]

with open("input", 'r') as f:
   bnums = [line.strip() for line in f.readlines()] 

for bnum in bnums:
    for i, digit in enumerate(bnum):
        counter[i] += int(digit)

for i, num in enumerate(counter):
    if num > len(bnums) / 2:
        print(i, num)
        gamma[i] = "1"
        epsilon[i] = "0"
    else:
        gamma[i] = "0"
        epsilon[i] = "1"

gamma_bin = "".join(gamma)
epsilon_bin = "".join(epsilon)

print(counter)
print(gamma_bin, epsilon_bin)
print(int(gamma_bin, 2) * int(epsilon_bin, 2))
