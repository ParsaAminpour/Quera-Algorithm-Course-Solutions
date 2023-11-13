import sys
def f():
    global base_2    
    zero_add = []
    one_add = []
    tmp_base = []
    base_2 = ['01','00','10','11']
    # base_2 = []
    z, o = '0', '1'
    i = 2
    while i < n:
        for elem in base_2:
            zero_add.append(z + elem)
            one_add.append(o + elem)
    
            
        tmp_base = [*zero_add, *list(reversed(one_add))]
        base_2 = tmp_base
        tmp_base = []
        zero_add = []
        one_add = []
        i += 1

if __name__ == '__main__':
    n = int(input())    
    if n == 2:
        print(*['00','01','11','10'], sep='\n')
        sys.exit()
    if n == 1:
        print('0','1', sep='\n')
        sys.exit()
        
    f()
    print(*base_2, sep='\n')
