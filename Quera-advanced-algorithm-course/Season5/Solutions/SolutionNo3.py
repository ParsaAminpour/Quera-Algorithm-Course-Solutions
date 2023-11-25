import numpy as np
# k -> init_energy
n ,k = map(int, input().split(' '))

friuts = []     #[[bi],[ai]] -> [- , +]
for i in range(n):
    data = list(map(int, input().split(' ')))
    friuts.append(data)

efficient_friuts_= np.array(list(filter(lambda x : x[0] < x[1], friuts)))
sorted_efficient_friuts = efficient_friuts_[np.argsort(efficient_friuts_[:, 0])]

results = []
init_energy = k
for f in sorted_efficient_friuts:
    if init_energy - f[0] >= 0:
        results.append(list(f))
        init_energy += abs(f[1]-f[0]) # abs is not necessary in here


result_friuts = list(map(lambda x : abs(x[0] - x[1]), results))

print(k + sum(result_friuts))