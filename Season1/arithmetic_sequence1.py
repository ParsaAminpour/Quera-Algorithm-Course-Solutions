# Solution for Exercise No.3 from Session No.1 of the course
import numpy as np

n, k = map(int, input().split(' '))
numbers = [x for x in map(int, input().split(' '))]

min_a = min(numbers) - ((n - 1)*k)
max_a = max(numbers)

operations_count = []
for i in range(min_a, max_a+1):
	arr_for_eval = np.arange(i, i+(n-1)*k+1, k)
	base_arr = numbers

	diff = np.subtract(base_arr, arr_for_eval)
	print(f"The eval arr is :{arr_for_eval} and the diff from base is {diff}")
	positive_diff = abs(diff)
	print(f"and the positive diff is {positive_diff} and sum is {positive_diff.sum()}\n")
	operations_count.append(positive_diff.sum())

print(min(operations_count))