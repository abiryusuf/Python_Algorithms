def anagram(a, b):
    a = a.lower()
    b = b.lower()

    x = sorted(a)
    y = sorted(b)
    if x == y:
        return True
    else:
        return False
print(anagram("abir", "yusuf"))

def anagram_1(s, r):
    s = s.lower()
    r = r.lower()
    if len(s) != len(r):
        return False
    count = {}

    for i in s:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    for x in r:
        if x in count:
            count[x] -=1
        else:
            count[x] = 1
    for k in count:
        if count[k] == 0:
            return True
    return False
print(anagram_1("abir", "aBir"))
