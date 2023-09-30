n = int(input()) # Btw, I'll use len(numbers)
numbers = list(map(int, input().split(' ')))
numbers.sort()

def finding_middle() -> int:
    if n % 2 == 1: 
        return numbers[int(len(numbers) / 2)]
    else:
        return numbers[int(len(numbers) / 2) - 1]
    
    return middle_numbers

def calculate_operations(mid:int) -> int:
    operations = 0
    for idx, elem in enumerate(numbers):
        if elem == mid : continue
        operations += abs(mid - elem)
    return operations
    
if __name__ == '__main__':
    middle_number = finding_middle()
    operation_count = calculate_operations(mid=middle_number)
    print(middle_number, operation_count, sep=' ')