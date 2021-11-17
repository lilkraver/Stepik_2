s, a, b = (input() for _ in range(3))

def f(s, a, b, counter=0):
    if a in b and a in s:
        return 'Impossible'
    if s == s.replace(a, b): 
        return counter
    else:
        counter += 1
        s = s.replace(a, b)
        return f(s, a, b, counter)

print(f(s, a, b))



s, a, b = [input() for i in range(3)]
count = 0

while a in s:
    if count == 1000:
        count = "Impossible"
        break
    s = s.replace(a, b)
    count += 1

print(count)
