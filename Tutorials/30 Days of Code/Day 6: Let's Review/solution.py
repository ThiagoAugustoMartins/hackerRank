t = int(input().strip())

result = []
for x in range(t):
    s = input().strip()
    even = []
    odd = []
    for index in range(len(s)):
        if index % 2 == 0:
            even.append(s[index])
        else:
            odd.append(s[index])
    result.append(even)
    result.append(odd)
    
for x in range(0, t):
    print("".join(result[x*2]) + " " + "".join(result[x*2+1]))