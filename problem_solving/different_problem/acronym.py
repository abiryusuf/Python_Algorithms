
info = "I am abir"
x = info.split()
print(x)

def myFun(str):
    str = str.split()
    res = ""

    for i in range(len(str)):
        word = str[i]
        res += word[0].upper()
    return res
print(myFun(info))

# for i in range(len(info)):
#     z = info[i]
#     print(z)

def reverse(str):
    res = ""
    for i in str:
        res = i + res
    return res
print(reverse(info))

def plaindron(str):
    new = ""
    rev = ""

    res = ""
    for i in str:
        if i != res:
            new = new + i
            rev = i + rev

    if new == rev:
        return True
    else:
        return False
print(plaindron("madam"))

arr = [2, 4, 5, 6, 6, 7, 7]

def dup(arr):
    res = []
    seen = set()
    for i in arr:
        if i not in seen:
            seen.add(i)
            res.append(i)
    return res
print(dup(arr))



