def anagram(str_1, str_2):
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    if len(str_1) == len(str_2):
        return True
    count = {}

    for x in str_1:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    for y in str_2:
        if y in count:
            count[y] -= 1
        else:
            count[y] = 1

    for k in count:
        if count[k] == 0:
            return True
    return False


    # x = sorted(str_1)
    # y = sorted(str_2)

    # if x == y:
    #     return True
    # else:
    #     return False
print(anagram("I am abir", "I am abir"))