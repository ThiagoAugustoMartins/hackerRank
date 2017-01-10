#!/bin/python3

import sys


n,c,m = input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = list(map(int, input().strip().split(' ')))

if m * c >= max(p):
    print("Yes")
else:
    print("No")