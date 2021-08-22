def split_and_join(line):
    a = line.split()
    b = "-".join(a)
    return b

print(split_and_join("this is string"))