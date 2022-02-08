print("Input:", end='')
a=input()
b=input()

la=''.join([i for i in a if not i.isdigit()])
lb=''.join([i for i in a if not i.isdigit()])
print(la)
print(lb)

if la!=lb:
    print("Output : Two expressions are identical")
elif la==lb:
    print("Output : Two expressions are different")