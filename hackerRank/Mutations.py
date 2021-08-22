string = "abracadabra"

print(string[5])

# it will show error but we can convert list then change the value

# string[3] ="x"
# print(string)

x = list(string)
x[5] = "k"
string = "".join(x)
print(string)

string = string[:4] + 'x' + string[5:]
print(string)

def mutate_string(str, index, char):
    x = list(str)
    x[index] = char
    str_1 = "".join(x)
    return str_1
    # slice
    # return string[:position] + character + string[position + 1:]
print(mutate_string("abracadabara", 5, "k"))