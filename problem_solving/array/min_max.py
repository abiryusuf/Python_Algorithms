
arr = [14, 11, 20, 3, 6, 7, 8, 5, 7, 11]


# for i in range(len(arr)):
#     x = i
#     print(x)


def maxNum(arr):
    max = arr[0]

    for i in range(len(arr)):
        current = arr[i]
        if current > max:
            max = current
    return max
print(maxNum(arr))

def min_max(arr):
    min = arr[0]
    max = arr[0]

    for i in range(len(arr)):
        current = arr[i]
        if current > max:
            max = current
        if current < min:
            min = current
    return "Smallest Number {} and Largest number {}".format(min, max)
print(min_max(arr))

def dup(arr):
    seen = set()
    new = []
    for i in range(len(arr)):
        if i not in seen:
            new.append(new[i])
            seen.add(i)
    return new
    # a = 0
    # new = set()
    #
    # while a < len(arr):
    #     new.add(arr[a])
    #     a += 1
    # return new
print(dup(arr))


def permute(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


string = "ABC"
n = len(string)
data = list(string)
permute(data, 0, n)