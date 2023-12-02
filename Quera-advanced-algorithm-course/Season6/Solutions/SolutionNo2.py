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
    
def sumation_subsets(sub:list) -> int:
    s = list(map(lambda set_ : sum(set_), sub))
    print(f"sumed: {s}\n\n")
    return max(s)

if __name__ == '__main__':
    n = int(input())
    numbers_list = [int(num) for num in input().split()]

    subset_extracted = extracting_subsets(numbers_list, n)

    max_result = sumation_subsets(subset_extracted)

    print(subset_extracted, sep='\n\n')
    print(max_result)