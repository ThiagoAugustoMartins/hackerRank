dict = {}

n = int(input().strip())

for x in range(n):
    name, number = input().strip().split()
    dict[name] = number

for x in range(n):
    name = input().strip()
    value = dict.get(name, "Not found")
    if value == "Not found":
        print("Not found")
    else:
        print(name + "=" + value)