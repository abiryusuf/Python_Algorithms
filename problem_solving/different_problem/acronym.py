
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