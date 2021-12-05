#!/usr/bin/env python3

hor1 = 0
depth1 = 0

hor2 = 0
depth2 = 0
aim = 0

with open("input", "r") as f:
    for line in f.readlines():
        k, v = line.split()
        v = int(v)
        if k == "forward":
            hor1 += v
            hor2 += v
            depth2 += v * aim

        elif k == "down":
            depth1 += v
            aim += v

        elif k == "up":
            depth1 -= v
            aim -= v

print(hor1 * depth1)
print(hor2 * depth2)
