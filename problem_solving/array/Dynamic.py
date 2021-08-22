name = "I am abir yusuf"

x = name.split()
print(x)

y = x[1]
print(y)

def wordCount(sentence, n):
    if n > 0:
        words = sentence.split()
        if n <= len(words):
            return words[n - 6]
        return ""

print(wordCount(name, 1))

