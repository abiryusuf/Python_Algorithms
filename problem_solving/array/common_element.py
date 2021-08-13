arr_1 = [1, 2, 4, 6, 7, 1]
arr_2 = [1, 3, 4, 6, 8, 1]

# output = [1, 4, 6]

def common_element(a, b):
    num1 = 0
    num2 = 0

    result = []

    while num1 < len(a) and num2 < len(b):
        if a[num1] == b[num2]:
            result.append(a[num1]) and result.append(b[num2])
            num1 += 1
            num2 += 1
        elif a[num1] < b[num2]:
            num1 += 1
        else:
            num2 += 1

    return result

print((common_element([1, 3, 4, 5, 5], [1, 2, 3, 4, 5, 5])))
print(common_element(arr_1, arr_2))

