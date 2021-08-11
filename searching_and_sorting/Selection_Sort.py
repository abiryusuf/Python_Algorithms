
# follow the order from smallest number
arr = [65, 25, 12, 33, 11]

for i in range(len(arr)):
     idx = i
     for j in range(i + 1, len(arr)):
         if arr[idx] > arr[j]:
             idx = j
     arr[i], arr[idx] = arr[idx], arr[i]
    # print(idx)
for i in range(len(arr)):
    print(arr[i])
for i, value in enumerate(arr):
    print("index {} and value {}".format(i + 1, value))

