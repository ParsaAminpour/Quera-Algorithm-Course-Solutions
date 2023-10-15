n, x = map(int, input().split(' '))
coefficients = list(map(int, input().split(' ')))
coefficients.reverse()

result = 0
for idx, a in enumerate(coefficients):
    result += a * x**idx


print(result % (1e9 + 7))

