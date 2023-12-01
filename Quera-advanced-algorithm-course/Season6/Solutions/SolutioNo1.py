def bottom_up(n:int) -> int:
    if n == 1: return 1
    
    b_u = [None] * (n)
    b_u[0], b_u[1] = 1, 2
    
    for i in range(2, n):
        b_u[i] = b_u[i-1] + b_u[i-2]
    
    return b_u[n-1]

if __name__ == '__main__':
    n = int(input())
    result = bottom_up(n)
    print(f"{int(result % (1e9 + 7))}")
