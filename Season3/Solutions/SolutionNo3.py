n, x = map(int, input().split(' '))
coefficients = list(map(int, input().split(' ')))
# coefficients.reverse()

# answers = []
# for i in range(n):
#     result = x * (answers[i]) + coefficients[i]
#     answers.append(result) #a0 , a1x, a2x^2 ,....
    
def horner_evaluation():
    result = 0
    for coefficient in coefficients[::-1]:
        result = result * x + coefficient
    return result

    
if __name__ == '__main__':
    answer = horner_evaluation()
    print(answer % int(1e9 + 7))

