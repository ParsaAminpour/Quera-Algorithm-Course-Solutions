n = int(input())

probs = 0
for i in range(1,n):
    for j in range(i,n):
        for k in range(j,n):
            if i + j > k and j + k > i and k + i > j:
                if i + j + k == n : probs += 1
                
print(probs)