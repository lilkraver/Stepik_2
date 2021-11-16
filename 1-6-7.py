def find_path(start, path):
    path.add(start)
    for node in graph[start]:
        if node not in path:
            find_path(node, path)

graph = {}
for i in range(int(input())):
    s = input().split()
    graph[s[0]] = s[2:] if len(s) > 1 else [s[0]]

for i in range(int(input())):
    s = input().split()
    path = set()
    find_path(s[1], path)
    print('Yes' if s[0] in path else 'No')
    
    
    
    
n = int(input())
pr = {}
for i in range(n):
    a = input().split()
    pr[a[0]] = a[2:]

for key in pr.keys():
    for value in pr[key]:
        if str(value) in pr:
            pr[key].extend(pr[value])

q = int(input())
for i in range(q):
    a = input().split()
    if a[0] in pr[a[1]] or a[0] == a[1]:
        print("Yes")
    else:
        print("No")
