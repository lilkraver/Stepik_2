s, t = input(), input()
count = 0
while len(s) >= len(t):
    if s.startswith(t):
        count += 1
        s = s[1:]
    else:
        s = s[1:]
print(count)



s, t = input(), input()
c = 0
while t in s:
	a = s.find(t)
	s = s[a+1:]
	c += 1

print(c)
