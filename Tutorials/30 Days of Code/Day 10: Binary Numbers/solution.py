n = int(input().strip())

n = bin(n)[2:]

result = 0
count = 0

for index, value in enumerate (n):
    if value == '1':
        count += 1
                    ## IF the last value is '1' the programm still have to test if it's bigger than the last value
    if value == '0' or index == len(n) - 1:
        if result < count:
            result = count
        count = 0

print(result)