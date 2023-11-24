n = int(input())
numbers = list(map(int, input().split(' ')))

        
for i in range(n):
    for j in range(0, n):
        if j == 0: continue
        if numbers[j] < numbers[j-1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            
print(*numbers, sep = ' ')