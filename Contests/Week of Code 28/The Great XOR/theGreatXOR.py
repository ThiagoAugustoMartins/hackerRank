#!/bin/python3

import sys

result = []
q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    total = 0
    for a in range(1, x):
        if a ^ x > x:  # x ^ y Does a "bitwise exclusive or"
            total += 1
    result.append(total)
    
for a0 in range(q):
    print(result[a0])
    