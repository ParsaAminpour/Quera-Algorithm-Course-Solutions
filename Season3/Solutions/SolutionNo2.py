n = int(input())
numbers = [int(x) for x in input().split()]

maxsum = ans = numbers[0]
for i in range(1, n):
    maxsum = max(maxsum+numbers[i],numbers[i])
    ans = max(ans, maxsum)
print(ans)