import sys
sys.setrecursionlimit(10**6)

n = int(input())
origin = [x for x in range(1,n+1)]  # e.g. [1,2,3]
destination = [] # B
helpful = [] # C

def _check_arange(seq:list) -> bool:
    return seq == sorted(seq)

step = 1
def cal():
    global step
    for i in range(n-1):
        helpful.append(origin[i])
        print(f"{step} A C")
        step += 1
        
    if _check_arange(helpful):    
        destination.append(origin[n-1])
        print(f"{step} A B")
        
        for k in range(n-1):
            destination.append(helpful[k])
            print(f"{step} C B")
            step += 1

# Way NO.2
def hanoi(n,src,dst,help):
    if n==1:
        print(step,src,dst)
        step+=1
    else:

        hanoi(n-1,src,help,dst) 
        print(step,src,dst)
        step+=1
        
        hanoi(n-1,help,dst,src)

if __name__ == '__main__':
    # cal()
    hanoi(n,'A','B','C')