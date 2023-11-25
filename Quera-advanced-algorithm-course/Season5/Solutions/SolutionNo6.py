n = int(input())
org_names = []
for i in range(n):
    org_names.append(input())
    
q = int(input())
info = set()
res = 0
for i in range(q):
    tmp = input()
    info.add(tmp)
    
    if len(info) == n:
        res += 1
        info.clear()
        info.add(tmp)
        
print(res)