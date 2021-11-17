import sys
import re

p1 = r'\b[10]+\b'
for line in sys.stdin:
    line = line.rstrip()
    if line.isdigit() and re.search(p1, line):
        k = re.findall(p1, line)
        for i in k:
            i = (int(i, 2))%3
            if i == 0:
                print(line)
