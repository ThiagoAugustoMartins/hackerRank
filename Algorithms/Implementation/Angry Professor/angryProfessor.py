t = int(input().strip())
for tests in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    result = 0
    for students in a:
        if students <= 0:
            result += 1
    if result >= k:
        print("NO") #Class is not canceled
    else:
        print("YES")    #Class is canceled