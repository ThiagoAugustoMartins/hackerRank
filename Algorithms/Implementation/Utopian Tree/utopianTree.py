t = int(input().strip())
for cycle in range(t):
    height = 1
    n = int(input().strip())
    for x in range(n):
        if x % 2 == 0:
            height *= 2
        else:
            height += 1
    print(height)