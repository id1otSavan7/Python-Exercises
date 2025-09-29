print(len("Hello World"))

def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]

for char in rev_str("Hello World"):
    print(char, end = '')


# Hello World
# d