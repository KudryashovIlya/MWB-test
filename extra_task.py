arr = [2, 7, 11, 15]
target = 9
all_pair = []

for num in arr:
    for x in range(0, len(arr) - 1):
        if num != arr[x+1]:
            all_pair.append([num, arr[x + 1]])

for result in all_pair:
    if sum(result) == target:
        print(arr.index(result[0]), arr.index(result[1]))
    elif (result[0] - result[1]) == target:
        print(arr.index(result[0]), arr.index(result[1]))
    elif (result[1] - result[0]) == target:
        print(arr.index(result[0]), arr.index(result[1]))

