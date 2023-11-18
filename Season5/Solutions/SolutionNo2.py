from rich import print
n, k = map(int, input().split(' '))
numbers = [int(num) for num in input().split()]

# max_len = n - (k-1)

# results = []
# tmp_list = []
# for r in range(k):
#     if r != 0 : results.append([numbers[r-1]])

#     for i in range(r, len(numbers)):
#         tmp_list.append(numbers[i])
        
#         if (i+1) % (max_len+r) == 0 or i == (len(numbers)-1): 
#             results.append(tmp_list)
#             tmp_list = []

# print(results)



class Solution:
    def __init__(self, n:int, k:int, numbers:list):
        self.n = n
        self.k = k
        self.numbers = numbers
        self.partition_count = 0
        self.start_idx = 0
        self.results = []
        self.max_len = n - (k - 1)

    # @param start_idx -> start_idx + 1
    def judge(self, start_idx:int, partition_count:int) -> list:
        rest_elemts_count = len(self.numbers) - start_idx
        if rest_elemts_count < self.max_len: # it's mean we reach to the end of elements which partition will create in strict mode
            rest_partition_len = k - self.partition_count

            for i in range(rest_partition_len):
                pass

            for i in range(start_idx, len(self.numbers)):
                self.results.append(self.numbers[i:rest_partition_len])
