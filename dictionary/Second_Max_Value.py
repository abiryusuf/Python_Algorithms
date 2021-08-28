# Python program to find second maximum value in Dictionary
new_dict ={"google":12, "amazon":9, "flipkart":4, "gfg":13}
# output 12

def maxValue(dict):
    max = 0

    for i in dict.values():
        if i > max:
            max = i
    return max - 2
print(maxValue(new_dict))

def secondMax(num):
    # maximum value
    max_1 = max(num.values())
    max_2 = 0
# iterate through the dictionary
    for i in num.values():
        if max_2 < i < max_1:
            max_2 = i
    return max_2
# print the second largest value
print(secondMax(new_dict))

