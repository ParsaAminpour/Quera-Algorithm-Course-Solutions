# in 15min
if __name__ == '__main__':
    n, c = map(int, input().split(' '))
    numbers = [int(num) for num in input().split()]
    numbers = list(reversed(sorted(numbers)))

    for i in range(len(numbers)):
        d = min(c, max(0, numbers[i] - c))
        c = c - d
        d = 0
        if c== 0: break

    print(c)