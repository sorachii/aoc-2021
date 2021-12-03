#!/usr/bin/env python3

with open("input", 'r') as f:
   scans = [int(line.strip()) for line in f.readlines()] 

counter, windows_counter = 0, 0

sum_of_windows = []
for i, line in enumerate(scans):
    if i < len(scans) - 2:
        sum_of_windows.append(sum(scans[i:i+3]))

for i, line in enumerate(scans):
    if i > 0 and line > scans[i-1]:
        counter += 1
    if  1998 > i > 0 and sum_of_windows[i] > sum_of_windows[i-1]:
        windows_counter += 1

print(counter)
print(windows_counter)
