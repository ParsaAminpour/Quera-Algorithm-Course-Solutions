from rich import print
n, k = map(int, input().split(' '))
numbers = [int(num) for num in input().split()]

partitions = []
tmp = []

for j in range(3):
    tmp_partitions = []
    tmp_partitions.append(numbers[:j])

    for i in range(j, len(numbers)):
        tmp.append(numbers[i])
        if (i+1-j) % k == 0 or i == len(numbers)-1:
            tmp_partitions.append(tmp)
            tmp = []

    partitions.append(tmp_partitions)
    tmp_partitions = []

print(partitions)



# sum_partitions = list(map(lambda x : sum(x), partitions))
# print(sum_partitions)

# print(min(sum_partitions))