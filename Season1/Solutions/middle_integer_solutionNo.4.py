n = int(input())
numbers = list(map(int, input().split(' ')))

O = {}
result = {}

def finding_middle_number() -> list:
    if len(numbers) == 2:
        middle_num = numbers[0]
        
    middle_num = numbers[int(len(numbers) / 2)] if len(numbers) % 2 == 1 else numbers[int(len(numbers) / 2)]
    return middle_num # correspond index -> int(len(numbers) / 2)
    
def calculate():
    idxs = [int(len(numbers) / 2) - 1, int(len(numbers) / 2), int(len(numbers) / 2) + 1]
    
    for middle_idx in idxs:
        tmp = 0
        for idx, elem in enumerate(numbers):
            if idx == middle_idx: continue
            tmp += abs(numbers[middle_idx] - elem)
        
        O[middle_idx] = tmp

def calculate_min():
    for key, value in O.items():
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)
    
    min_results = result[min(result.keys())]
    return min(min_results)

if __name__ == "__main__":
    calculate()
    choiced = calculate_min()
    print(numbers[choiced], min(result.keys()))
