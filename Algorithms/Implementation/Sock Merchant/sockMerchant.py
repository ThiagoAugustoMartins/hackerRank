n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

total = 0
array_temp = []
for item in c:
    if item in array_temp:
        array_temp.remove(item)
        total += 1
    else:
        array_temp.append(item)
        
print(total)