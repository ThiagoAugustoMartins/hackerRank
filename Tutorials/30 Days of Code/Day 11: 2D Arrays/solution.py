data = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   data.append(arr_t)

h_data = []
for row in range(len(data) - 2):
    for collumn in range(len(data) - 2):
        hourglass = data[row][collumn] + data[row][collumn + 1] + data[row][collumn + 2] + data[row + 1][collumn + 1] + data[row + 2][collumn] + data[row + 2][collumn + 1] + data[row + 2][collumn + 2]
        h_data.append(hourglass)

print(max(h_data))