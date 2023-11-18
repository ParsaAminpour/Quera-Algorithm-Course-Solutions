n, k = map(int, input().split())
a = list(map(int, input().split()))
sum = 0

for i in range(n):
    a[i] = a[i]-i*k
    sum = sum + a[i]

a.sort()

psum = 0
ans = -1

for i in range(n):
    temp = (a[i]*i - psum)
    psum = psum + a[i]
    temp = temp + (sum - psum - a[i]*(n - 1 - i))
    if ans == -1 or temp < ans:
        ans = temp

print(ans)