m = []
for k in objects:
    ident = id(k)
    m.append(ident)
amount = set(m)
print(len(amount))
