import numpy as np

def extracting_subsets(set_:list, n_:int) -> list:
    results = []
    for mask in range(1 << n_):
        tmp_result = []
        for j in range(n):
            if mask & (1 << j):
                tmp_result.append(set_[j])
        results.append(tmp_result)
        tmp_result = []
    
    return results

def arrays_different(a, b):
    # Check if arrays have no common elements
    a_set = set(a)
    b_set = set(b)
    
    if not (a_set & b_set): return True
    else: return False

    
def partition_subsets(sub:list) -> list:
    partition = []
    for i in range(len(sub)):
        for j in range (i, len(sub)):
            # partition rules
            if len(sub[j]) == n - len(sub[i]) and arrays_different(sub[i],sub[j]):
                partition.append([sub[i], sub[j]])

    return partition


def sum_each_subset(subsets: list) -> list:
    sum_results = []
    for sub in subsets:
        sum_results.append([sum(sub[0]), sum(sub[1])])
    
    return sum_results


def get_min_diff(sum_data:list) -> int:
    diffs = list(map(lambda x : abs(x[0]-x[1]), sum_data))
    print(f"diffs:\n{diffs}\n")
    return min(diffs)


if __name__ == '__main__': # prints are for logging (shouldn't use in main answer)
    n = int(input())
    numbers_list = [int(num) for num in input().split()]

    subset_extracted = extracting_subsets(numbers_list, n)
    print(f"subset_extracted:\n{subset_extracted}\n")

    partition_base = partition_subsets(subset_extracted)
    print(f"partition_base:\n{partition_base}\n")

    sumation_of_subsets = sum_each_subset(partition_base)
    print(f"sumation_of_subsets:\n{sumation_of_subsets}\n")

    answer = get_min_diff(sumation_of_subsets)
    print(answer)