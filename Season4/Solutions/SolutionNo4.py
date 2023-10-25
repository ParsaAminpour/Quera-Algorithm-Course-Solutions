import sys
sys.setrecursionlimit(10**6)

def base(bin_:str, m:int) -> str:
    base_binary = [0 for z in range(m - len(bin_))]
    for num in bin_:
        base_binary.append(int(num))
    return base_binary

results = []
def cal(n:int):
    for j in range(2**n):
        binary_result = bin(j)[2:]
        correction = base(binary_result, n)

        results.append("".join(map(str,correction)))
        


# Way No.2
updated_bins = []
base_bins = ['01','00','10','11']

def numeric_cal(new_base, m:int):
    tmp_bins = []
    
    for j in range(m-2):
        # step A 
        for b in new_base:
            tmp_bins.append(f"0{b}")
            updated_bins.append(tmp_bins)
            tmp_bins = []
            
    # step B in reversed
        for b_ in reversed(new_base):
            tmp_bins.append(f"1{b_}")
            updated_bins.append(tmp_bins)
            tmp_bins = []
        
            
    

if __name__ == '__main__':
    n = int(input())
    numeric_cal(base_bins, n)
    # main = [int(res) for res in results]
    print(updated_bins[-1][0])