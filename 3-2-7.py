import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    p = r"cat"
    m = re.findall(p, line)
    if len(m) > 1:
        print(line)
