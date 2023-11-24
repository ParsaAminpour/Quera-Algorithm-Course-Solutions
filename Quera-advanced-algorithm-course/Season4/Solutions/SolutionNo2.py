import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())


# way No.1
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
    

# Way Nn.2 (Not appropriate for large numbers)
def gcd(m,n):
    if m == n: return m
    if m*n == 0: return 0

    if m > n:
        tmp = m - n
        if m % tmp == 0: return tmp
        else : return gcd(n, tmp)
    
    else:
        tmp = n - m
        if n % tmp == 0: return tmp
        else: return gcd(m ,tmp)

# Way No.3 (Appropriate for large numbers to calculate gcd)
def gcd2(m, n):
    while n:
        m, n = n, m % n
    return m



if __name__ == '__main__':
    result = gcd2(a,b)
    print(result)
    
    