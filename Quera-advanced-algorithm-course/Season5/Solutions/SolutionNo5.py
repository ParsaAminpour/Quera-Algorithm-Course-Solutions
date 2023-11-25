n = int(input())
ranges = []
for i in range(n):
    r = [int(num) for num in input().split()]
    ranges.append(r)

sorted_ranges = sorted(ranges, key=lambda x : x[0])
main_ranges = sorted(sorted_ranges, key = lambda x : x[1])

R = main_ranges[0][1]
count = 1
for i in range(1, len(main_ranges)):
    if main_ranges[i][0] >= R:
        count += 1
        R = main_ranges[i][1]
    

print(count)