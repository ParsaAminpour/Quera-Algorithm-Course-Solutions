import sys

answers = []
def cal(m:int):
    for j in range(2**m):
        answers.append(bin(j)[2:])

def base(_answers:list) -> list:
    return list(map(lambda x : x.zfill(n), answers))
    
if __name__ == '__main__':
    n = int(input())
    cal(n)
    result = base(answers)
    print(*result, sep='\n')
