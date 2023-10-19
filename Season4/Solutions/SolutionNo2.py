import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())


def f(m, n):
    if m == n: return m
    if m*n == 0: return 0
    
    if m > n:
        x = m % n
        if x == 0 or n % x == 0: return x
        else: return f(x, n)
    else:
        x = n % m
        if x == 0 or m % x == 0: return x
        else: return f(m, x) 
    
    
if __name__ == '__main__':
    result = f(a,b)
    print(result)
    
    