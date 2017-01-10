n = int(input())
values = input()

array = []
array = values.split()
arrayMode = []
mean = 0
median = 0
mode = 0

#Calculating the mean
for x in range(0, len(array)):
    array[x] = float(array[x])
    mean += array[x]
mean = mean/n

#Ordering the values of the array
for y in range(0, len(array)):
    for x in range(0, len(array) - 1):
        if x != len(array) - 1:
            if array[x] > array[x+1]:
                array[x], array[x+1] = array[x+1], array[x]
#print(array)
#Calculating the median || Seeing if the size of the array is even or odd
if len(array)%2 == 0:
    median = (array[int(len(array)/2)] + array[int(len(array)/2 - 1)]) / 2
else:
    median = array[len(array)/2 + 1/2]

k = 1

for x in range(0, len(array) - 1):
    if array[x] == array[x+1]:
        k += 1
        arrayMode.append(k)
    else:
        k = 1
        arrayMode.append(k)

if max(arrayMode) == 1:
    mode = array[0]
else:
    for x in range(len(arrayMode)):
        if arrayMode[x] == max(arrayMode):
            mode = array[x]
            break
    
#print(arrayMode)
    
print("{0:.1f}".format(mean))
print(median)
print(int(mode))