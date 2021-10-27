str = "ac"

def uniqueStr(str):
    res = set()

    for i in str:
        if i in res:
            return False
        else:
            res.add(i)
    return True
print(uniqueStr(str))