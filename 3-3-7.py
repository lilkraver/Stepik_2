import requests
import re

text = requests.get(input()).text
domains = re.findall(r'<a.* href="(?:\w+://){0,1}(\w[\w\.-]+).*"',text)
domains = sorted(set(domains))
print(*domains, sep='\n')



import re
import requests

pattern = r'''(?:\<a.*href\=['"])(?:\w+\:\/\/)?(\w+[\.\-\w+]*)'''
f = requests.get(input().rstrip())
urls = []

for ur in re.findall(pattern, f.text):
    if ur not in urls:
        urls.append(ur)

urls.sort()
print(*urls, sep='\n')
