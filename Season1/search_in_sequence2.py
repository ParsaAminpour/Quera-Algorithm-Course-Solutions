n, q = map(int, input().split())

a = [x for x in map(int, input().split(' '))]
a.sort()

questions = []
for i in range(q):
    num = int(input())
    questions.append(num)


# Search (binary O(log n)) for the max(a) from question to remove extra data
max_q = max(questions)
idx = 0
if max_q == a[len(a)//2]: idx = len(a)//2 

if max_q > a[len(a)//2]:
    for i in range(len(a)//2, len(a)):
        if max_q == a[i]: idx = i
        if max_q > a[i]: idx = i
# Optimized a is:
opt_a = a[:idx+1]   

print(opt_a)

answers = []
default = 0 
for y in questions:
    for x in opt_a:
        if x < y: default += 1

    answers.append(default)
    default = 0

print(*answers, sep='\n')
