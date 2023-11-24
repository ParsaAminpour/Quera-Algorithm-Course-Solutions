n = int(input())    

props = 0

for i in range(1, n):
    for j in range(1, n):
        k = n - (i + j)
        if k < 1:
            continue
        print(i, j, k)
        if i + j > k and j + k > i and k + i > j:
            if i + j + k == n : props += 1
            
print(props)