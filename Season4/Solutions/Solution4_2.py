answers = []

def another_way2(m:int):
    for j in range(2**m):
        answers.append(bin(j)[2:])

def output(_answers:list):
    return list(map(lambda x : x.zfill(n), answers))
    
    
if __name__ == '__main__':
    n = int(input())
    another_way2(n)
    result = output(answers)
    print(*result, sep='\n')
