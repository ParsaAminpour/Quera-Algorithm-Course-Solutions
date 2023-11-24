import sys
sys.setrecursionlimit(10**6)

n = int(input())

def cal(k:int):
    if k == 0: return 5
    
    tmp = cal(k-1)
    
    if k % 2 == 0:
        return tmp - 21
    else:
        return tmp * tmp
        
if __name__ == '__main__':
    print(cal(n))
    
        