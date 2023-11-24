n = int(input())
result = 0
for a in range(1,(n//3) + 1):
    result += (n - 3 * a) // 2 - max(0, n // 2 - 2 * a + 1) + 1
print(result)