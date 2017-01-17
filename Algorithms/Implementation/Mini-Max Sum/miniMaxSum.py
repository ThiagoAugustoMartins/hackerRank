numbers = [int(x) for x in input().strip().split()]

print(sum(numbers) - max(numbers), sum(numbers) - min(numbers))
