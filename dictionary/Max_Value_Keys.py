
# Python program to find Maximum value from dictionary whose key is present in the list
test_dict = {"Gfg": 4, "is": 5, "best": 9,
             "for": 11, "geeks": 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing list
test_list = ["Gfg", "best", "geeks"]

res = 0
for i in test_list:
    if i in test_dict:
        res = max(res, test_dict[i])
print(res)

def maxFun(num):
    max = 0
    for i in range(len(num)):
        cur = num[i]
        if cur > max:
            max = cur
    return max
print(maxFun(test_dict))