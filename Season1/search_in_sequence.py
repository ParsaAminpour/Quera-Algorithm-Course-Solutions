# Solution for Exercise No.1 belongs Session No.1
n, q = map(int, input().split())

numbers = [x for x in map(int, input().split(' '))]

x = []
for i in range(q):
    x.append(int(input()))

# procccess
answers = []
for j in x:
    result = len([n for n in numbers if n < j])
    answers.append(result)

print(*answers, sep='\n')

