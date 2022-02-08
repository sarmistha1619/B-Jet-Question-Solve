def rec(n):
    v = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]
    for i in n:
        if i in v:
            n = n.replace(i, '')

    l = ''.join([i for i in n if not i.isdigit()])
    for i in l:
        print("*", end="")
        print(i.upper(), end="")
n = input("Input:")
rec(n)