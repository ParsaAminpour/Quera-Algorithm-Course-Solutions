n = int(input())
numbers = list(map(int, input().split(' ')))

amounts = []

for i in range(len(numbers)):
	for j in range(i, len(numbers)):
		amounts.append(sum(numbers[i:j+1]))
		

print(max(amounts))


