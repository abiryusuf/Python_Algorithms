def countLetter(str):
    str = str.replace(" ", "").lower()
    count = {}

    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(countLetter("abir yusuf"))

