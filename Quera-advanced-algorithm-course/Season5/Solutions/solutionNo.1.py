n = int(input())
tasks = [int(num) for num in input().split()]
tasks = sorted(tasks)

def cal():
    counter = 0
    time_origin = 0
    for i in range(len(tasks)):
        if time_origin < tasks[i]:
            counter += 1
            time_origin += 1
    return counter
            
if __name__ == '__main__':
    result = cal()
    print(result)