arr = [3, 5, 6, 10]

def missingElement(arr):
    temp = []
    for i in range(max(arr) + 1):
        if i not in arr:
            temp.append(i)
    return temp
print(missingElement(arr))

res = [x for x in range(max(arr) + 1) if x not in arr]

print(res)